from module.Module import Module
import json as js
from data_manager import data_manager
            
class Calendar(Module):
    def __init__(self, list, response):
        self.responseObject = response
        super().__init__(list)
        self.data_response = data_manager.get_response_templates()
        self.last_shown_activities = []  # Lưu list activities được show gần nhất

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
        elif self.list['verbs'] in ['complete', 'finish', 'done']:
            pass
        elif self.list['verbs'] in ['incomplete', 'unfinish', 'undo']:
                pass
        else:
            print('invalid')
        return 
    
    def return_response(self):
        response = ""
        data_response = self.data_response
        
        # GROUP VERBS
        SHOW_VERBS = ['show', 'check', 'tell']
        COMPLETE_VERBS = ['complete', 'finish', 'done']
        INCOMPLETE_VERBS = ['incomplete', 'unfinish', 'undo']

        if self.list.get("location"):
            if self.responseObject.isContinue:
                self.responseObject.isContinue = False
                response = data_response['wrong_input']['retry_process']
            else:
                response = data_response["wrong_input"]["missing_object"]
         # ============ INCOMPLETE BY INDEX ============
        elif self.list.get('verbs') in INCOMPLETE_VERBS and self.list.get('index'):
            index = self.list['index']
            
            # ✅ Đọc từ MongoDB nếu memory rỗng
            if not self.last_shown_activities:
                temp_data = data_manager.get_temp_data()
                if temp_data and 'last_shown_activities' in temp_data:
                    self.last_shown_activities = temp_data['last_shown_activities']
            
            print(f"🔍 DEBUG Complete by index:")
            print(f"   - Index: {index}")
            print(f"   - Last shown activities: {len(self.last_shown_activities)} items")
            
            # Kiểm tra xem có danh sách activities không
            if not self.last_shown_activities:
                response = "No activity list found. Please run 'show calendar' first to see the numbered list."
            elif index < 1 or index > len(self.last_shown_activities):
                response = f"Invalid index. Please choose a number between 1 and {len(self.last_shown_activities)}."
            else:
                # Lấy activity theo index (index - 1 vì list bắt đầu từ 0)
                activity = self.last_shown_activities[index - 1]
                
                # Complete activity này
                event_filter = {
                    'date': activity['date'],
                    'type': activity['type'],
                    'description': activity['description'],
                    'start_time': activity['start_time']
                }
                
                count = data_manager.incomplete_calendar_event(event_filter)
                
                if count > 0:
                    response = f"Incompleted: {activity['type'].upper()} - {activity['description']} ({activity['start_time']} - {activity.get('end_time', 'N/A')})"
                else:
                    response = "Failed to incomplete the activity."
         # ============ INCOMPLETE ALL EVENT/MEETING ============
        elif self.list.get('verbs') in INCOMPLETE_VERBS:
            if self.list['objects'] in ['event', 'meeting']:
                if self.list.get('date'):
                    # Incomplete tất cả events/meetings trong ngày đó
                    event_filter = {
                        'date': self.list['date'],
                        'type': self.list['objects'],
                        'completed': {'$ne': False}
                    }
                    count = data_manager.incomplete_calendar_event(event_filter)
                    
                    if count > 0:
                        response = f"Marked {count} {self.list['objects']}(s) as incompleted on {self.list['date']}."
                    else:
                        response = f"No completed {self.list['objects']} found on {self.list['date']}."
                else:
                    response = (
                    "Please tell me the date of the meeting you want to undo.\n"
                    "For example: \"Incomplete meeting on 01/01/2025\"."
                   )

            elif self.list['objects'] == 'calendar':
                response = "Please specify whether you want to complete an 'event' or 'meeting'."
            
            else:
                response = data_response["wrong_input"]["missing_object"]
        # ============ COMPLETE BY INDEX ============
        elif self.list.get('verbs') in COMPLETE_VERBS and self.list.get('index'):
            index = self.list['index']
            
            # ✅ Đọc từ MongoDB nếu memory rỗng
            if not self.last_shown_activities:
                temp_data = data_manager.get_temp_data()
                if temp_data and 'last_shown_activities' in temp_data:
                    self.last_shown_activities = temp_data['last_shown_activities']
            
            print(f"🔍 DEBUG Complete by index:")
            print(f"   - Index: {index}")
            print(f"   - Last shown activities: {len(self.last_shown_activities)} items")
            
            # Kiểm tra xem có danh sách activities không
            if not self.last_shown_activities:
                response = "No activity list found. Please run 'show calendar' first to see the numbered list."
            elif index < 1 or index > len(self.last_shown_activities):
                response = f"Invalid index. Please choose a number between 1 and {len(self.last_shown_activities)}."
            else:
                # Lấy activity theo index (index - 1 vì list bắt đầu từ 0)
                activity = self.last_shown_activities[index - 1]
                
                # Complete activity này
                event_filter = {
                    'date': activity['date'],
                    'type': activity['type'],
                    'description': activity['description'],
                    'start_time': activity['start_time']
                }
                
                count = data_manager.complete_calendar_event(event_filter)
                
                if count > 0:
                    response = f"Completed: {activity['type'].upper()} - {activity['description']} ({activity['start_time']} - {activity.get('end_time', 'N/A')})"
                else:
                    response = "Failed to complete the activity."
        
        # ============ COMPLETE ALL EVENT/MEETING ============
        elif self.list.get('verbs') in COMPLETE_VERBS:
            if self.list['objects'] in ['event', 'meeting']:
                if self.list.get('date'):
                    # Complete tất cả events/meetings trong ngày đó
                    event_filter = {
                        'date': self.list['date'],
                        'type': self.list['objects'],
                        'completed': {'$ne': True}
                    }
                    count = data_manager.complete_calendar_event(event_filter)
                    
                    if count > 0:
                        response = f"Marked {count} {self.list['objects']}(s) as completed on {self.list['date']}."
                    else:
                        response = f"No incomplete {self.list['objects']} found on {self.list['date']}."
                else:
                      response = (
                    "Please tell me the date of the meeting you want to mark completed.\n"
                    "For example: \"Complete meeting on 01/01/2025\"."
                   )

            elif self.list['objects'] == 'calendar':
                response = "Please specify whether you want to complete an 'event' or 'meeting'."
            
            else:
                response = data_response["wrong_input"]["missing_object"]
        
        # ============ EVENT/MEETING (SHOW/SET) ============
        elif self.list['objects'] in ['event', 'meeting'] and self.responseObject.isContinue == False:
            if self.list.get('verbs') in SHOW_VERBS and self.list.get('date'):
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
                        # Lưu list vào MongoDB để complete sau
                        self.last_shown_activities = filtered_activities
                        data_manager.save_temp_data({
                            'last_shown_activities': filtered_activities
                        })
                        response = self._format_activities_as_cards(
                            filtered_activities, 
                            self.list['date']
                        )

            elif self.list.get('verbs') == 'set' and self.list.get('date'):
                if not self.list.get('start_time'):
                    response = data_response['wrong_input']['wrong_time']
                elif not self.responseObject.isContinue:
                    response = data_response['calendar']['add_title']
                    self.responseObject.isContinue = True

            else:
                response = data_response['wrong_input']["missing_date"]

        # ============ CALENDAR ============
        elif self.list['objects'] == 'calendar':
            if self.list.get('verbs') in SHOW_VERBS and self.list.get('date'):
                activities = self.get_activities_for_date(self.list['date'])
                
                if not activities:
                    response = data_response['calendar']['no_activity'].format(
                        objects='activity', 
                        date=self.list['date']
                    )
                else:
                    # Lưu list vào MongoDB để complete sau
                    self.last_shown_activities = activities
                    data_manager.save_temp_data({
                        'last_shown_activities': activities
                    })
                    response = self._format_activities_as_cards(
                        activities, 
                        self.list['date']
                    )
                        
            elif self.list.get('verbs') == 'set':
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
                "completed": False
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
        """
        filters = {"date": date}
        events = data_manager.get_calendar_events(filters=filters)
        
        if not events:
            return []
            
        return events
    
    def _format_activities_as_cards(self, activities, date):
        """
        Format activities thành card CÓ SỐ THỨ TỰ
        """
        if not activities:
            return f"You have no activity on {date}."
        
        result = f"📅 Your schedule for {date}:\n"
        result += "_" * 96 + "\n\n"
        
        for idx, activity in enumerate(activities, start=1):  # Thêm số thứ tự
            activity_type = activity.get('type', 'activity')
            title = activity.get('description', 'Untitled')
            start = activity.get('start_time', 'N/A')
            end = activity.get('end_time', 'N/A')
            completed = activity.get('completed', False)
            
            # Icon theo type
            if activity_type == 'event':
                icon = '📅'
            elif activity_type == 'meeting':
                icon = '🤝'
            else:
                icon = '📌'
            
            # Status icon
            status_icon = '✅' if completed else '☐'
            
            # ✅ Build card với số thứ tự
            result += f"[{idx}] {status_icon} {activity_type.upper()}\n"
            result += f"     Title: {title}\n"
            result += f"     Time:  {start} - {end}\n"
            
            # if completed:
            #     result += f"     Status: COMPLETED ✓\n"
            
            result += "_" * 96 + "\n\n"
        
        result += f"\n💡 Tip: Type 'complete [number]' to mark an activity as done (e.g., 'complete 1')\n"
        
        return result