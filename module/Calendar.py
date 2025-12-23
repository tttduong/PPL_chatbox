from module.Module import Module
import json as js
from data_manager import data_manager
            
class Calendar(Module):
    def __init__(self, list, response):
        self.responseObject = response
        super().__init__(list)
        self.data_response = data_manager.get_response_templates()
        self.pending_action = None  #pending wait for deleting 
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
        elif self.list['verbs'] in ['delete' , 'remove' , 'cancel']:
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
        DELETE_VERBS = ['delete', 'remove', 'cancel']
        STATUS_INCOMPLETE = ['incompleted', 'pending']
        STATUS_COMPLETE = ['completed', 'done']

        if self.list.get("location"):
            if self.responseObject.isContinue:
                self.responseObject.isContinue = False
                response = data_response['wrong_input']['retry_process']
            else:
                response = data_response["wrong_input"]["missing_object"]
        
        # ============ SHOW INCOMPLETE TASKS ============
        elif (self.list.get('verbs') in SHOW_VERBS and 
              self.list.get('status_filter') in STATUS_INCOMPLETE):
            
            # Get incomplete events with optional date filter
            filters = {'completed': {'$ne': True}}
            
            if self.list.get('date'):
                filters['date'] = self.list['date']
            
            # Filter by type if specified
            if self.list.get('objects') in ['event', 'meeting']:
                filters['type'] = self.list['objects']
            
            incomplete_activities = data_manager.get_calendar_events(filters=filters)
            
            if not incomplete_activities:
                if self.list.get('date'):
                    response = f"No incomplete tasks found on {self.list['date']}."
                else:
                    response = "You have no incomplete tasks! Great job! 🎉"
            else:
                # Save to memory for later operations
                self.last_shown_activities = incomplete_activities
                data_manager.save_temp_data({
                    'last_shown_activities': incomplete_activities
                })
                
                # Format response
                if self.list.get('date'):
                    response = self._format_incomplete_tasks(incomplete_activities, self.list['date'])
                else:
                    response = self._format_incomplete_tasks(incomplete_activities)
        
        # ============ SHOW COMPLETED TASKS ============
        elif (self.list.get('verbs') in SHOW_VERBS and 
              self.list.get('status_filter') in STATUS_COMPLETE):
            
            # Get completed events with optional date filter
            filters = {'completed': True}
            
            if self.list.get('date'):
                filters['date'] = self.list['date']
            
            # Filter by type if specified
            if self.list.get('objects') in ['event', 'meeting']:
                filters['type'] = self.list['objects']
            
            completed_activities = data_manager.get_calendar_events(filters=filters)
            
            if not completed_activities:
                if self.list.get('date'):
                    response = f"No completed tasks found on {self.list['date']}."
                else:
                    response = "You have no completed tasks yet."
            else:
                # Save to memory
                self.last_shown_activities = completed_activities
                data_manager.save_temp_data({
                    'last_shown_activities': completed_activities
                })
                
                # Format response
                if self.list.get('date'):
                    response = self._format_completed_tasks(completed_activities, self.list['date'])
                else:
                    response = self._format_completed_tasks(completed_activities)
        
        # ============ DELETE BY INDEX ============
        elif self.list.get('verbs') in DELETE_VERBS and self.list.get('index'):
            index = self.list['index']

            if not self.last_shown_activities:
                temp_data = data_manager.get_temp_data()
                if temp_data and 'last_shown_activities' in temp_data:
                    self.last_shown_activities = temp_data['last_shown_activities']

            if not self.last_shown_activities:
                response = "No activity list found. Please run 'show calendar' first to see the numbered list."
            elif index < 1 or index > len(self.last_shown_activities):
                response = f"Invalid index. Please choose a number between 1 and {len(self.last_shown_activities)}."
            else:
                activity = self.last_shown_activities[index - 1]

                # 🔐 LƯU pending delete
                self.pending_action = {
                    'action': 'delete',
                    'activity': activity
                }

                response = (
                    f"Are you sure you want to delete this {activity['type']}?\n"
                    f"{activity['description']} "
                    f"({activity['start_time']} - {activity.get('end_time', 'N/A')})\n"
                    "Please reply with 'yes' or 'no'."
                )
        
        # ============ CONFIRM DELETE ============
        elif self.pending_action and self.pending_action.get('action') == 'delete':
            if self.list.get('verbs') in ['yes', 'confirm', 'ok']:
                activity = self.pending_action['activity']

                event_filter = {
                    'date': activity['date'],
                    'type': activity['type'],
                    'description': activity['description'],
                    'start_time': activity['start_time']
                }

                count = data_manager.delete_calendar_event(event_filter)
                self.pending_action = None

                if count > 0:
                    response = (
                        f"Deleted: {activity['type'].upper()} - "
                        f"{activity['description']} "
                        f"({activity['start_time']} - {activity.get('end_time', 'N/A')})"
                    )
                else:
                    response = "Failed to delete the activity."

            elif self.list.get('verbs') in ['no', 'cancel']:
                self.pending_action = None
                response = "Deletion cancelled."

            else:
                response = "Please reply with 'yes' or 'no'."

        # ============ INCOMPLETE BY INDEX ============
        elif self.list.get('verbs') in INCOMPLETE_VERBS and self.list.get('index'):
            index = self.list['index']
            
            if not self.last_shown_activities:
                temp_data = data_manager.get_temp_data()
                if temp_data and 'last_shown_activities' in temp_data:
                    self.last_shown_activities = temp_data['last_shown_activities']
            
            if not self.last_shown_activities:
                response = "No activity list found. Please run 'show calendar' first to see the numbered list."
            elif index < 1 or index > len(self.last_shown_activities):
                response = f"Invalid index. Please choose a number between 1 and {len(self.last_shown_activities)}."
            else:
                activity = self.last_shown_activities[index - 1]
                
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
            
            if not self.last_shown_activities:
                temp_data = data_manager.get_temp_data()
                if temp_data and 'last_shown_activities' in temp_data:
                    self.last_shown_activities = temp_data['last_shown_activities']
            
            if not self.last_shown_activities:
                response = "No activity list found. Please run 'show calendar' first to see the numbered list."
            elif index < 1 or index > len(self.last_shown_activities):
                response = f"Invalid index. Please choose a number between 1 and {len(self.last_shown_activities)}."
            else:
                activity = self.last_shown_activities[index - 1]
                
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
        
        for idx, activity in enumerate(activities, start=1):
            activity_type = activity.get('type', 'activity')
            title = activity.get('description', 'Untitled')
            start = activity.get('start_time', 'N/A')
            end = activity.get('end_time', 'N/A')
            completed = activity.get('completed', False)
            
            if activity_type == 'event':
                icon = '📅'
            elif activity_type == 'meeting':
                icon = '🤝'
            else:
                icon = '📌'
            
            status_icon = '✅' if completed else '☐'
            
            result += f"[{idx}] {status_icon} {activity_type.upper()}\n"
            result += f"     Title: {title}\n"
            result += f"     Time:  {start} - {end}\n"
            result += "_" * 96 + "\n\n"
        
        result += f"\n💡 Tip: Type 'complete [number]' to mark an activity as done (e.g., 'complete 1')\n"
        
        return result
    
    def _format_incomplete_tasks(self, activities, date=None):
        """
        Format incomplete tasks với số thứ tự và nhóm theo ngày
        """
        if not activities:
            return "You have no incomplete tasks! 🎉"
        
        if date:
            result = f"📝 Incomplete tasks for {date}:\n"
        else:
            result = f"📝 All incomplete tasks:\n"
        
        result += "_" * 96 + "\n\n"
        
        # Group by date if showing all
        if not date:
            from collections import defaultdict
            grouped = defaultdict(list)
            for activity in activities:
                grouped[activity['date']].append(activity)
            
            idx = 1
            for task_date in sorted(grouped.keys()):
                result += f"📆 {task_date}================================================ "
                for activity in grouped[task_date]:
                    result += self._format_single_task(activity, idx)
                    idx += 1
                result += "\n"
        else:
            for idx, activity in enumerate(activities, start=1):
                result += self._format_single_task(activity, idx)
        
        result += f"\n💡 Tip: Type 'complete [number]' to mark a task as done\n"
        result += f"💡 Tip: Type 'delete [number]' to remove a task\n"
        
        return result
    
    def _format_completed_tasks(self, activities, date=None):
        """
        Format completed tasks với số thứ tự
        """
        if not activities:
            return "No completed tasks found."
        
        if date:
            result = f"✅ Completed tasks for {date}:\n"
        else:
            result = f"✅ All completed tasks:\n"
        
        result += "_" * 96 + "\n\n"
        
        # Group by date if showing all
        if not date:
            from collections import defaultdict
            grouped = defaultdict(list)
            for activity in activities:
                grouped[activity['date']].append(activity)
            
            idx = 1
            for task_date in sorted(grouped.keys()):
                result += f"📆 {task_date}================================================ "
                for activity in grouped[task_date]:
                    result += self._format_single_task(activity, idx, completed=True)
                    idx += 1
                result += "\n"
        else:
            for idx, activity in enumerate(activities, start=1):
                result += self._format_single_task(activity, idx, completed=True)
        
        result += f"\n💡 Tip: Type 'incomplete [number]' to unmark a task\n"
        
        return result
    
    def _format_single_task(self, activity, idx, completed=False):
        """
        Format một task duy nhất
        """
        activity_type = activity.get('type', 'activity')
        title = activity.get('description', 'Untitled')
        start = activity.get('start_time', 'N/A')
        end = activity.get('end_time', 'N/A')
        
        if activity_type == 'event':
            icon = '📅'
        elif activity_type == 'meeting':
            icon = '🤝'
        else:
            icon = '📌'
        
        status_icon = '✅' if completed else '☐'
        
        result = f"[{idx}] {status_icon} {activity_type.upper()}\n"
        result += f"     Title: {title}\n"
        result += f"     Time:  {start} - {end}\n"
        result += "_" * 96 + "\n\n"
        
        return result