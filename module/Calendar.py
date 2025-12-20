from module.Module import Module
import json as js
from data_manager import data_manager
            
class Calendar(Module):
    def __init__(self, list, response):
        self.responseObject = response
        super().__init__(list)
        self.data_response = data_manager.get_response_templates()

    def take_action(self):
        """ 
        Parameter: 
            None
        Action:
            do action base on verbs
        Return:
            None
        """
        if self.list['verbs'] == 'show':
            pass
        elif self.list['verbs'] == 'set':
            pass
        elif self.list['verbs'] in ['complete', 'finish', 'done']:  # ✅ THÊM
            pass
        else:
            print('invalid')
        return 
    def return_response(self):
            response = ""
            data_response = self.data_response
            
            # ✅ GROUP VERBS
            SHOW_VERBS = ['show', 'check', 'tell']
            COMPLETE_VERBS = ['complete', 'finish', 'done']
            
            if self.list.get("location"):
                if self.responseObject.isContinue:
                    self.responseObject.isContinue = False
                    response = data_response['wrong_input']['retry_process']
                else:
                    response = data_response["wrong_input"]["missing_object"]
                    
            # ============ COMPLETE EVENT/MEETING ============
            elif self.list['verbs'] in COMPLETE_VERBS:
                if self.list['objects'] in ['event', 'meeting']:
                    if self.list.get('date'):
                        # Complete tất cả events/meetings trong ngày đó
                        event_filter = {
                            'date': self.list['date'],
                            'type': self.list['objects'],
                            'completed': {'$ne': True}  # Chỉ complete những cái chưa complete
                        }
                        count = data_manager.complete_calendar_event(event_filter)
                        
                        if count > 0:
                            response = f"✅ Marked {count} {self.list['objects']}(s) as completed on {self.list['date']}."
                        else:
                            response = f"No incomplete {self.list['objects']} found on {self.list['date']}."
                    else:
                        # Complete event/meeting gần nhất
                        event_filter = {
                            'type': self.list['objects'],
                            'completed': {'$ne': True}
                        }
                        count = data_manager.complete_calendar_event(event_filter)
                        
                        if count > 0:
                            response = f"✅ Marked the latest {self.list['objects']} as completed."
                        else:
                            response = f"No incomplete {self.list['objects']} found."
                
                elif self.list['objects'] == 'calendar':
                    response = "Please specify whether you want to complete an 'event' or 'meeting'."
                
                else:
                    response = data_response["wrong_input"]["missing_object"]
            
            # ============ EVENT/MEETING (SHOW/SET) ============
            elif self.list['objects'] in ['event', 'meeting'] and self.responseObject.isContinue == False:
                if self.list['verbs'] in SHOW_VERBS and self.list.get('date'):
                    # ✅ SỬA: Lấy cả incomplete và completed events
                    activities = self.get_activities_for_date(self.list['date'])
                    
                    if not activities:
                        response = data_response['calendar']['no_activity'].format(
                            objects=self.list['objects'], 
                            date=self.list['date']
                        )
                    else:
                        filtered_activities = [
                            activity for activity in activities 
                            if activity['type'] == self.list['objects']
                        ]
                        
                        if not filtered_activities:
                            response = data_response['calendar']['no_activity'].format(
                                objects=self.list['objects'], 
                                date=self.list['date']
                            )
                        else:
                            response = self._format_activities_as_cards(
                                filtered_activities, 
                                self.list['date']
                            )

                elif self.list['verbs'] == 'set' and self.list.get('date'):
                    if not self.list.get('start_time'):
                        response = data_response['wrong_input']['wrong_time']
                    elif not self.responseObject.isContinue:
                        response = data_response['calendar']['add_title']
                        self.responseObject.isContinue = True

                else:
                    response = data_response['wrong_input']["missing_date"]

            # ============ CALENDAR ============
            elif self.list['objects'] == 'calendar':
                if self.list['verbs'] in SHOW_VERBS and self.list.get('date'):
                    activities = self.get_activities_for_date(self.list['date'])
                    
                    if not activities:
                        response = data_response['calendar']['no_activity'].format(
                            objects='activity', 
                            date=self.list['date']
                        )
                    else:
                        response = self._format_activities_as_cards(
                            activities, 
                            self.list['date']
                        )
                            
                elif self.list['verbs'] == 'set':
                    response = data_response['wrong_input']['missing_object']
                else:
                    response = data_response['wrong_input']["missing_date"]
                    
            # ============ ADD TITLE ============
            elif self.list.get('title'):
                self.responseObject.isContinue = False
                data_temp = data_manager.get_temp_data() 
                
                event_data = {
                    "date": data_temp['date'],
                    "type": data_temp['objects'],
                    "description": self.list['title'],
                    "start_time": data_temp['start_time'],
                    "end_time": data_temp.get('end_time'),
                    "location": data_temp.get('location'),
                    "completed": False  # ✅ Mặc định là chưa complete
                }
                
                event_id = data_manager.save_calendar_event(event_data)
                
                if event_id:
                    response = data_response['calendar']['finish_set'].format(
                        objects=data_temp['objects'], 
                        title=self.list['title'], 
                        date=data_temp['date']
                    )
                else:
                    response = "Error: Failed to save event to MongoDB."
            
            else:
                if self.responseObject.isContinue:
                    self.responseObject.isContinue = False
                    response = data_response['wrong_input']['retry_process']
                else:
                    response = data_response["wrong_input"]["missing_object"]

            return response
    def get_activities_for_date(self, date): 
        """
        Lấy các hoạt động cho một ngày từ MongoDB.
        Luôn trả về một danh sách (list), có thể là rỗng, thay vì trả về 'No_date'.
        """
        filters = {"date": date}
        events = data_manager.get_calendar_events(filters=filters)
        
        if not events:
            return [] # Trả về danh sách rỗng thay vì 'No_date'
            
        return events
    
    def _format_activities_as_cards(self, activities, date):
        """
        Format activities thành card, hiển thị status completed/incomplete
        """
        if not activities:
            return f"You have no activity on {date}."
        
        result = f"📅 Your schedule for {date}:\n"
        result += "_" * 96 + "\n\n"
        
        for activity in activities:
            activity_type = activity.get('type', 'activity')
            title = activity.get('description', 'Untitled')
            start = activity.get('start_time', 'N/A')
            end = activity.get('end_time', 'N/A')
            completed = activity.get('completed', False)  # ✅ Kiểm tra completed status
            
            # Icon theo type
            if activity_type == 'event':
                icon = '📅'
            elif activity_type == 'meeting':
                icon = '🤝'
            else:
                icon = '📌'
            
            # ✅ Status icon
            status_icon = '✅' if completed else '☐'
            
            # Build card
            # result += f"{status_icon} {icon} {activity_type.upper()} \n"
            result += f"{status_icon} {activity_type.upper()} \n"

            result += f"   Title: {title}\n"
            result += f"   Time:  {start} - {end}\n"
            
            if completed:
                result += f"   Status: COMPLETED ✓\n"
            
            result += "_" * 96 + "\n\n"
        
        return result
        
    # def return_response(self):
    #     """ 
    #     Parameter: 
    #         None
    #     Action:
    #         specify data
    #     Return:
    #         response message
    #     """
    #     response = ""
    #     # Sử dụng template đã load sẵn
    #     data_response = self.data_response
    #     # data_response = js.load(open("data/Data_Response.json"))
    #     if self.list.get("location"):
    #         if self.responseObject.isContinue:
    #             self.responseObject.isContinue = False
    #             response = data_response['wrong_input']['retry_process']
    #         else:
    #             response = data_response["wrong_input"]["missing_object"]
    #     elif self.list['objects'] in ['event', 'meeting'] and self.responseObject.isContinue == False:
    #         if self.list['verbs'] == 'show' and self.list.get('date'):
    #             activities = self.get_activities_for_date(self.list['date'])
    #             if activities == 'No_date':
    #                 response = data_response['calendar']['date_out_of_bound']
    #             else:
    #                 response = "\n".join([f"You have {activity['type']}: \"{activity['description']}\", start at {activity.get('start_time', 'N/A')} and end at {activity.get('end_time', 'N/A')}." for activity in activities if activity['type'] == self.list['objects']])
    #                 if not response:
    #                     response = data_response['calendar']['no_activity'].format(objects=self.list['objects'], date=self.list['date'])

    #         elif self.list['verbs'] == 'set' and self.list.get('date'):
    #             activities = self.get_activities_for_date(self.list['date'])
    #             if activities == 'No_date':
    #                 response = data_response['calendar']['date_out_of_bound']
    #             # elif (not self.list.get('start_time')) or (not self.list.get('end_time') and self.list['objects'] == 'meeting') or ("invalid_input" in [self.list['start_time'], self.list.get('end_time')]) or (self.list['start_time'] > (self.list['end_time'] if self.list.get('end_time') else "25:60")):
    #             #     response = data_response['wrong_input']['wrong_time']

    #             # CODE MỚI ĐÃ SỬA (Giúp dữ liệu vượt qua bước kiểm tra)--------------
    #             elif (not self.list.get('start_time')):
    #                     response = data_response['wrong_input']['wrong_time']
    #             #----------------------------------------------------------
    #             elif not self.responseObject.isContinue:
    #                 response = data_response['calendar']['add_title']
    #                 self.responseObject.isContinue = True

    #         else:
    #             response = data_response['wrong_input']["missing_date"]

    #     elif self.list['objects'] == 'calendar':
    #         if self.list['verbs'] == 'show' and self.list.get('date'):
    #             activities = self.get_activities_for_date(self.list['date'])
    #             if activities == 'No_date':
    #                 response = data_response['calendar']['date_out_of_bound']
    #             else:
    #                 response = "\n".join([f"You have {activity['type']}: \"{activity['description']}\", start at {activity.get('start_time', 'N/A')} and end at {activity.get('end_time', 'N/A')}." for activity in activities])
    #                 if not response:
    #                     response = data_response['calendar']['no_activity'].format(objects='activity', date=self.list['date'])
    #         elif self.list['verbs'] == 'set':
    #             response = data_response['wrong_input']['missing_object']
    #         else:
    #             response = data_response['wrong_input']["missing_date"]
                
    #     elif self.list.get('title'):
    #         self.responseObject.isContinue = False
    #         # LẤY DATA TẠM THỜI TỪ MONGO (thay vì file JSON)
    #         # data_temp là dictionary chứa các thông tin date, objects, start_time...
    #         data_temp = data_manager.get_temp_data() 
            
    #         # CHUẨN BỊ EVENT DATA CHO MONGO DB (không cần lặp qua schedule nữa)
    #         event_data = {
    #             "date": data_temp['date'],
    #             "type": data_temp['objects'],
    #             "description": self.list['title'], # Title là input mới nhất
    #             "start_time": data_temp['start_time'],
    #             "end_time": data_temp.get('end_time'),
    #             # Bạn có thể thêm location nếu nó được lưu trong data_temp
    #             "location": data_temp.get('location') 
    #         }
            
    #         # GỌI HÀM SAVE_CALENDAR_EVENT TỪ DATA_MANAGER
    #         event_id = data_manager.save_calendar_event(event_data)
            
    #         if event_id:
    #             response = data_response['calendar']['finish_set'].format(
    #                 objects=data_temp['objects'], 
    #                 title=self.list['title'], 
    #                 date=data_temp['date']
    #             )
    #         else:
    #              response = "Error: Failed to save event to MongoDB."
    #         #  ------------------------------------------------------------------
    #         # data_temp = js.load(open("data/Data_temp.json"))
    #         # data = js.load(open("data/Data_Calendar.json"))
    #         # for day in data['schedule']:
    #         #     if day['date'] == data_temp['date']:
    #         #         day['activities'].append({
    #         #             "type": data_temp['objects'],
    #         #             "description": self.list['title'],
    #         #             "start_time": data_temp['start_time'],
    #         #             "end_time": data_temp.get('end_time')
    #         #         })
    #         #         break
    #         # try: 
    #         #     with open("data/Data_Calendar.json", 'w') as f: 
    #         #         js.dump(data, f, indent=4) 
    #         #     print(f"Activities saved to Data_Calendar") 
    #         # except Exception as e: 
    #         #     print(f"Failed to save activities: {e}")
    #         # response = data_response['calendar']['finish_set'].format(objects=data_temp['objects'], title=self.list['title'], date=data_temp['date'])
    #     else:
    #         if self.responseObject.isContinue:
    #             self.responseObject.isContinue = False
    #             response = data_response['wrong_input']['retry_process']
    #         else:
    #             response = data_response["wrong_input"]["missing_object"]

    #     return response
    
    def get_activities_for_date(self, date): 
        """
        Lấy các hoạt động cho một ngày từ MongoDB.
        Luôn trả về một danh sách (list), có thể là rỗng, thay vì trả về 'No_date'.
        """
        filters = {"date": date}
        events = data_manager.get_calendar_events(filters=filters)
        
        # Nếu data_manager.get_calendar_events trả về danh sách rỗng (thường là [])
        # thì chúng ta vẫn trả về danh sách rỗng đó.
        if not events:
            return [] # THAY ĐỔI LỚN: Trả về danh sách rỗng thay vì 'No_date'
            
        # Nếu có sự kiện, trả về danh sách sự kiện
        return events
        # data = js.load(open("data/Data_Calendar.json"))
        # for day in data['schedule']: 
        #     if day['date'] == date: 
        #         return day['activities']
        # return 'No_date'
    


# from module.Module import Module
# import json as js
# from data_manager import data_manager
            
# class Calendar(Module):
#     def __init__(self, list, response):
#         self.responseObject = response
#         super().__init__(list)
#         self.data_response = data_manager.get_response_templates()

#     def take_action(self):
#         if self.list['verbs'] == 'show':
#             pass
#         elif self.list['verbs'] == 'set':
#             pass
#         else:
#             print('invalid')
#         return 
    
#     def return_response(self):
#         response = ""
#         data_response = self.data_response
        
#         if self.list.get("location"):
#             if self.responseObject.isContinue:
#                 self.responseObject.isContinue = False
#                 response = data_response['wrong_input']['retry_process']
#             else:
#                 response = data_response["wrong_input"]["missing_object"]
                
#         # ============ EVENT/MEETING ============
#         elif self.list['objects'] in ['event', 'meeting'] and self.responseObject.isContinue == False:
#             # --- SHOW ---
#             if self.list['verbs'] == 'show' and self.list.get('date'):
#                 activities = self.get_activities_for_date(self.list['date'])
                
#                 # ✅ FIX: Kiểm tra list rỗng thay vì string 'No_date'
#                 if not activities:
#                     response = data_response['calendar']['no_activity'].format(
#                         objects=self.list['objects'], 
#                         date=self.list['date']
#                     )
#                 else:
#                     # Filter theo type (meeting hoặc event)
#                     filtered = [
#                         f"You have {activity['type']}: \"{activity['description']}\", "
#                         f"start at {activity.get('start_time', 'N/A')} and "
#                         f"end at {activity.get('end_time', 'N/A')}." 
#                         for activity in activities 
#                         if activity['type'] == self.list['objects']
#                     ]
                    
#                     if filtered:
#                         response = "\n".join(filtered)
#                     else:
#                         response = data_response['calendar']['no_activity'].format(
#                             objects=self.list['objects'], 
#                             date=self.list['date']
#                         )
            
#             # --- SET ---
#             elif self.list['verbs'] == 'set' and self.list.get('date'):
#                 # ✅ FIX: Không cần check activities nữa vì MongoDB tự động xử lý
                
#                 # Kiểm tra start_time
#                 if not self.list.get('start_time'):
#                     response = data_response['wrong_input']['wrong_time']
#                 elif not self.responseObject.isContinue:
#                     response = data_response['calendar']['add_title']
#                     self.responseObject.isContinue = True
            
#             # --- MISSING DATE ---
#             else:
#                 response = data_response['wrong_input']["missing_date"]

#         # ============ CALENDAR ============
#         elif self.list['objects'] == 'calendar':
#             # --- SHOW ---
#             if self.list['verbs'] == 'show' and self.list.get('date'):
#                 activities = self.get_activities_for_date(self.list['date'])
                
#                 # ✅ FIX: Kiểm tra list rỗng
#                 if not activities:
#                     response = data_response['calendar']['no_activity'].format(
#                         objects='activity', 
#                         date=self.list['date']
#                     )
#                 else:
#                     response = "\n".join([
#                         f"You have {activity['type']}: \"{activity['description']}\", "
#                         f"start at {activity.get('start_time', 'N/A')} and "
#                         f"end at {activity.get('end_time', 'N/A')}." 
#                         for activity in activities
#                     ])
            
#             # --- SET (INVALID) ---
#             elif self.list['verbs'] == 'set':
#                 response = data_response['wrong_input']['missing_object']
            
#             # --- MISSING DATE ---
#             else:
#                 response = data_response['wrong_input']["missing_date"]
                
#         # ============ ADD TITLE ============
#         elif self.list.get('title'):
#             self.responseObject.isContinue = False
#             data_temp = data_manager.get_temp_data() 
            
#             event_data = {
#                 "date": data_temp['date'],
#                 "type": data_temp['objects'],
#                 "description": self.list['title'],
#                 "start_time": data_temp['start_time'],
#                 "end_time": data_temp.get('end_time'),
#                 "location": data_temp.get('location') 
#             }
            
#             event_id = data_manager.save_calendar_event(event_data)
            
#             if event_id:
#                 response = data_response['calendar']['finish_set'].format(
#                     objects=data_temp['objects'], 
#                     title=self.list['title'], 
#                     date=data_temp['date']
#                 )
#             else:
#                 response = "Error: Failed to save event to MongoDB."
        
#         # ============ DEFAULT ============
#         else:
#             if self.responseObject.isContinue:
#                 self.responseObject.isContinue = False
#                 response = data_response['wrong_input']['retry_process']
#             else:
#                 response = data_response["wrong_input"]["missing_object"]

#         return response
    
#     def get_activities_for_date(self, date): 
#         """
#         ✅ Lấy các hoạt động cho một ngày từ MongoDB.
#         Luôn trả về list (có thể rỗng).
#         """
#         filters = {"date": date}
#         events = data_manager.get_calendar_events(filters=filters)
#         return events if events else []