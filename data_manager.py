# data_manager.py
# quản lý việc đọc, ghi file 
import json
from datetime import datetime
from config_mongodb import mongodb

class DataManager:
    """Quản lý data với MongoDB thay vì JSON files"""
    
    def __init__(self):
        self.db = mongodb.get_db()
        # Collections mapping
        self.collections = {
            'temp': 'temp_data',           # Thay thế Data_temp.json
            'calendar': 'data_calendar',   # Thay thế Data_Calendar.json
            'pomodoro': 'data_pomodoro',   # Thay thế Data_Pomodoro.json
            'response': 'data_response_data',   # Thay thế Data_Response.json
            'weather': 'weather_data'      # Thay thế weather_data.json
        }
    
    def save_temp_data(self, data):
        """
        Lưu temporary data (thay thế việc ghi Data_temp.json)
        """
        try:
            collection = self.db[self.collections['temp']]
            
            # Thêm timestamp
            data['timestamp'] = datetime.now()
            data['session_id'] = self._get_session_id()
            
            # Insert document
            result = collection.insert_one(data)
            print(f"✅ Temp data saved with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"❌ Failed to save temp data: {e}")
            return None
    
    def get_temp_data(self, session_id=None):
        """
        Lấy temporary data (thay thế việc đọc Data_temp.json)
        """
        try:
            collection = self.db[self.collections['temp']]
            
            if session_id:
                data = collection.find_one({'session_id': session_id})
            else:
                # Lấy data mới nhất
                data = collection.find_one(sort=[('timestamp', -1)])
            
            if data:
                data.pop('_id', None)  # Remove MongoDB ID
            return data
        except Exception as e:
            print(f"❌ Failed to get temp data: {e}")
            return None
    
    def save_calendar_event(self, event_data):
        """
        Lưu calendar event vào MongoDB
        """
        try:
            collection = self.db[self.collections['calendar']]
            event_data['created_at'] = datetime.now()
            result = collection.insert_one(event_data)
            print(f"✅ Calendar event saved with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"❌ Failed to save calendar event: {e}")
            return None
    
    def get_calendar_events(self, filters=None):
        """
        Lấy calendar events với filters (date, type, etc.)
        """
        try:
            collection = self.db[self.collections['calendar']]
            query = filters if filters else {}
            events = list(collection.find(query).sort('created_at', -1))
            
            # Remove MongoDB _id
            for event in events:
                event.pop('_id', None)
            
            return events
        except Exception as e:
            print(f"❌ Failed to get calendar events: {e}")
            return []
    
    def get_response_templates(self):
        """
        Lấy response templates (thay thế Data_Response.json)
        """
        try:
            collection = self.db[self.collections['response']]
            
            # Check if templates exist
            templates = collection.find_one({'type': 'templates'})
            
            if not templates:
                # Nếu chưa có, migrate từ file JSON cũ
                self._migrate_response_templates()
                templates = collection.find_one({'type': 'templates'})
            
            if templates:
                templates.pop('_id', None)
                return templates.get('data', {})
            
            return {}
        except Exception as e:
            print(f"❌ Failed to get response templates: {e}")
            return {}
    
  
    def _get_session_id(self):
        """Generate session ID (có thể dùng user ID nếu có authentication)"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def _migrate_response_templates(self):
        """
        Migration: Chuyển Data_Response.json sang MongoDB (chỉ chạy 1 lần)
        """
        try:
            with open('data/Data_Response.json', 'r', encoding='utf-8') as f:
                response_data = json.load(f)
            
            collection = self.db[self.collections['response']]
            collection.insert_one({
                'type': 'templates',
                'data': response_data,
                'migrated_at': datetime.now()
            })
            print("✅ Response templates migrated to MongoDB")
        except FileNotFoundError:
            print("⚠️ Data_Response.json not found, skipping migration")
        except Exception as e:
            print(f"❌ Migration failed: {e}")
    
    def clear_temp_data(self, older_than_hours=24):
        """Xóa temp data cũ hơn X giờ"""
        try:
            collection = self.db[self.collections['temp']]
            cutoff_time = datetime.now() - timedelta(hours=older_than_hours)
            result = collection.delete_many({'timestamp': {'$lt': cutoff_time}})
            print(f"✅ Deleted {result.deleted_count} old temp records")
        except Exception as e:
            print(f"❌ Failed to clear temp data: {e}")

    #RELATED COMPLETION TASK FUNCTION
    def complete_calendar_event(self, event_filter):
        """
        Đánh dấu event là completed
        
        Args:
            event_filter: dict chứa filter để tìm event
                        Ví dụ: {'date': '20/12/2025', 'type': 'meeting'}
                        hoặc: {'description': 'Team standup'}
        
        Returns:
            int: Số lượng events đã complete
        """
        try:
            collection = self.db[self.collections['calendar']]
            
            # Update event với completed flag
            result = collection.update_many(
                event_filter,
                {
                    '$set': {
                        'completed': True,
                        'completed_at': datetime.now()
                    }
                }
            )
            
            print(f"✅ Marked {result.modified_count} event(s) as completed")
            return result.modified_count
        except Exception as e:
            print(f"❌ Failed to complete event: {e}")
            return 0

    def get_incomplete_events(self, filters=None):
        """
        Lấy danh sách events chưa complete
        
        Args:
            filters: dict chứa filter bổ sung (date, type, etc.)
        
        Returns:
            list: Danh sách events chưa complete
        """
        try:
            collection = self.db[self.collections['calendar']]
            
            # Base query: chỉ lấy event chưa complete
            query = {'completed': {'$ne': True}}
            
            # Thêm filters nếu có
            if filters:
                query.update(filters)
            
            events = list(collection.find(query).sort('created_at', -1))
            
            # Remove MongoDB _id
            for event in events:
                event.pop('_id', None)
            
            return events
        except Exception as e:
            print(f"❌ Failed to get incomplete events: {e}")
            return []

    def incomplete_calendar_event(self, event_filter):
        """
        Đánh dấu event là chưa hoàn thành (undo complete)
        
        Args:
            event_filter: dict chứa filter để tìm event
        
        Returns:
            int: Số lượng events đã uncomplete
        """
        try:
            collection = self.db[self.collections['calendar']]
            
            result = collection.update_many(
                event_filter,
                {
                    '$set': {'completed': False},
                    '$unset': {'completed_at': ''}
                }
            )
            
            print(f"✅ Unmarked {result.modified_count} event(s) as incomplete")
            return result.modified_count
        except Exception as e:
            print(f"❌ Failed to uncomplete event: {e}")
            return 0
    def delete_calendar_event(self, filters):
        """
        Delete calendar event(s) based on filters
        
        Args:
            filters (dict): MongoDB query filters
            
        Returns:
            int: Number of deleted documents
            
        Example:
            # Delete by specific event
            filters = {
                'date': '22/12/2025',
                'type': 'event',
                'description': 'Team Meeting',
                'start_time': '09:00'
            }
            count = data_manager.delete_calendar_event(filters)
            
            # Delete all events on a date
            filters = {
                'date': '22/12/2025',
                'type': 'event'
            }
            count = data_manager.delete_calendar_event(filters)
        """
        try:
            collection = self.db[self.collections['calendar']]  
            result = collection.delete_many(filters)
            print(f"✅ Deleted {result.deleted_count} event(s)")
            return result.deleted_count
        except Exception as e:
            print(f"❌ Error deleting events: {e}")
            return 0
# Singleton instance
data_manager = DataManager()