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
        else:
            print('invalid')
        return 
    
    def return_response(self):
        """ 
        Parameter: 
            None
        Action:
            specify data
        Return:
            response message
        """
        response = ""
        # Sử dụng template đã load sẵn
        data_response = self.data_response
        # data_response = js.load(open("data/Data_Response.json"))
        if self.list.get("location"):
            if self.responseObject.isContinue:
                self.responseObject.isContinue = False
                response = data_response['wrong_input']['retry_process']
            else:
                response = data_response["wrong_input"]["missing_object"]
        elif self.list['objects'] in ['event', 'meeting'] and self.responseObject.isContinue == False:
            if self.list['verbs'] == 'show' and self.list.get('date'):
                activities = self.get_activities_for_date(self.list['date'])
                if activities == 'No_date':
                    response = data_response['calendar']['date_out_of_bound']
                else:
                    response = "\n".join([f"You have {activity['type']}: \"{activity['description']}\", start at {activity.get('start_time', 'N/A')} and end at {activity.get('end_time', 'N/A')}." for activity in activities if activity['type'] == self.list['objects']])
                    if not response:
                        response = data_response['calendar']['no_activity'].format(objects=self.list['objects'], date=self.list['date'])

            elif self.list['verbs'] == 'set' and self.list.get('date'):
                activities = self.get_activities_for_date(self.list['date'])
                if activities == 'No_date':
                    response = data_response['calendar']['date_out_of_bound']
                # elif (not self.list.get('start_time')) or (not self.list.get('end_time') and self.list['objects'] == 'meeting') or ("invalid_input" in [self.list['start_time'], self.list.get('end_time')]) or (self.list['start_time'] > (self.list['end_time'] if self.list.get('end_time') else "25:60")):
                #     response = data_response['wrong_input']['wrong_time']

                # CODE MỚI ĐÃ SỬA (Giúp dữ liệu vượt qua bước kiểm tra)--------------
                elif (not self.list.get('start_time')):
                        response = data_response['wrong_input']['wrong_time']
                #----------------------------------------------------------
                elif not self.responseObject.isContinue:
                    response = data_response['calendar']['add_title']
                    self.responseObject.isContinue = True

            else:
                response = data_response['wrong_input']["missing_date"]

        elif self.list['objects'] == 'calendar':
            if self.list['verbs'] == 'show' and self.list.get('date'):
                activities = self.get_activities_for_date(self.list['date'])
                if activities == 'No_date':
                    response = data_response['calendar']['date_out_of_bound']
                else:
                    response = "\n".join([f"You have {activity['type']}: \"{activity['description']}\", start at {activity.get('start_time', 'N/A')} and end at {activity.get('end_time', 'N/A')}." for activity in activities])
                    if not response:
                        response = data_response['calendar']['no_activity'].format(objects='activity', date=self.list['date'])
            elif self.list['verbs'] == 'set':
                response = data_response['wrong_input']['missing_object']
            else:
                response = data_response['wrong_input']["missing_date"]
                
        elif self.list.get('title'):
            self.responseObject.isContinue = False
            # LẤY DATA TẠM THỜI TỪ MONGO (thay vì file JSON)
            # data_temp là dictionary chứa các thông tin date, objects, start_time...
            data_temp = data_manager.get_temp_data() 
            
            # CHUẨN BỊ EVENT DATA CHO MONGO DB (không cần lặp qua schedule nữa)
            event_data = {
                "date": data_temp['date'],
                "type": data_temp['objects'],
                "description": self.list['title'], # Title là input mới nhất
                "start_time": data_temp['start_time'],
                "end_time": data_temp.get('end_time'),
                # Bạn có thể thêm location nếu nó được lưu trong data_temp
                "location": data_temp.get('location') 
            }
            
            # GỌI HÀM SAVE_CALENDAR_EVENT TỪ DATA_MANAGER
            event_id = data_manager.save_calendar_event(event_data)
            
            if event_id:
                response = data_response['calendar']['finish_set'].format(
                    objects=data_temp['objects'], 
                    title=self.list['title'], 
                    date=data_temp['date']
                )
            else:
                 response = "Error: Failed to save event to MongoDB."
            #  ------------------------------------------------------------------
            # data_temp = js.load(open("data/Data_temp.json"))
            # data = js.load(open("data/Data_Calendar.json"))
            # for day in data['schedule']:
            #     if day['date'] == data_temp['date']:
            #         day['activities'].append({
            #             "type": data_temp['objects'],
            #             "description": self.list['title'],
            #             "start_time": data_temp['start_time'],
            #             "end_time": data_temp.get('end_time')
            #         })
            #         break
            # try: 
            #     with open("data/Data_Calendar.json", 'w') as f: 
            #         js.dump(data, f, indent=4) 
            #     print(f"Activities saved to Data_Calendar") 
            # except Exception as e: 
            #     print(f"Failed to save activities: {e}")
            # response = data_response['calendar']['finish_set'].format(objects=data_temp['objects'], title=self.list['title'], date=data_temp['date'])
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
    


