from CompiledFiles.ChatGrammarLexer import ChatGrammarLexer
from CompiledFiles.ChatGrammarParser import ChatGrammarParser
from ExtractorVisitor import ExtractorVisitor
from antlr4 import *
from module.Calendar import Calendar
# from module.Weather import Weather
# from module.Pomodoro import Pomodoro
import json as js
from data_manager import data_manager  # ✅ IMPORT MongoDB manager

class Response():
    def __init__(self):
        self.isContinue = False
        pass
    
    def get_response(self, input):
        """ 
        Parameter: 
            input -> input message from user
        Action:
            remove punctuation and redundant words
            create tree
            create elements list
            (for continue: input won't be pre-processed)
        Return:
            message response from check_input()
        """
        if not self.isContinue:
            pre_process = pre_processing(input)
            input_stream = InputStream(pre_process)
            lexer = ChatGrammarLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = ChatGrammarParser(stream)
            tree = parser.program()
            visitor = ExtractorVisitor()
            elements_list = visitor.visit(tree)
            print(elements_list)
        else:
            input_stream = InputStream(input)
            lexer = ChatGrammarLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = ChatGrammarParser(stream)
            tree = parser.program()
            visitor = ExtractorVisitor()
            elements_list = visitor.visit(tree)
            print(elements_list)
        return self.check_input(elements_list)

    def get_list(self, input):
        """ 
        Parameter: 
            input -> input message from user
        Action:
            remove punctuation and redundant words
            create tree
            create elements list
        Return:
            elements list
        """
        pre_process = pre_processing(input)
        input_stream = InputStream(pre_process)
        lexer = ChatGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ChatGrammarParser(stream)
        tree = parser.program()
        visitor = ExtractorVisitor()
        elements_list = visitor.visit(tree)
        return elements_list

    def check_input(self, list):
        """ 
        Parameter: 
            list -> elements list
        Action:
            create object for response handling
        Return:
            message response from object
        """
        # Handle incomplete/unfinish with index (no objects)
        if list.get('verbs') in ['incomplete', 'unfinish', 'undo'] and list.get('index'):
            list['objects'] = 'calendar'  # Set default object
            object = Calendar(list=list, response=self)
            return object.return_response()
        # Handle complete/finish/done with index (no objects)
        if list.get('verbs') in ['complete', 'finish', 'done'] and list.get('index'):
            list['objects'] = 'calendar'  # Set default object
            object = Calendar(list=list, response=self)
            return object.return_response()
        
        # Handle any command with index but no objects, supposing that user are intẻacting with calendar
        if list.get('index') and not list.get('objects'):
            list['objects'] = 'calendar'  # Assume calendar operation
            object = Calendar(list=list, response=self)
            return object.return_response()
    
        # ✅ CALENDAR/MEETING/EVENT
        if (list.get("objects") in ['meeting', 'calendar', 'event']):
            object = Calendar(list=list, response=self)
            try:
                if not self.isContinue:
                    # ✅ LƯU VÀO MONGODB thay vì Data_temp.json
                    result = data_manager.save_temp_data(list)
                    if result:
                        print(f"✅ Activities saved to MongoDB (ID: {result})")
                    else:
                        print("⚠️ Failed to save to MongoDB, falling back to file")
                        # Fallback: vẫn lưu file nếu MongoDB fail
                        with open('data/Data_temp.json', 'w') as f: 
                            js.dump(list, f, indent=4)
            except Exception as e: 
                print(f"❌ Failed to save activities: {e}")
                # Fallback to file
                try:
                    with open('data/Data_temp.json', 'w') as f: 
                        js.dump(list, f, indent=4)
                except:
                    pass
            return object.return_response()
        
        # ✅ WEATHER
        # elif list.get("objects") == "weather" and list.get("location"):
        #     weather = Weather(list=list)
        #     response = weather.return_response()
            
        #     # ✅ LƯU WEATHER DATA VÀO MONGODB (optional, để cache)
        #     try:
        #         weather_data = {
        #             'location': list.get('location'),
        #             'query': list,
        #             'response': response
        #         }
        #         data_manager.save_weather_data(weather_data)
        #     except Exception as e:
        #         print(f"⚠️ Failed to cache weather data: {e}")
            
        #     return response
        
        # ✅ POMODORO
        # elif list.get("objects") == "pomodoro":
        #     object = Pomodoro(list=list)
        #     return object.return_response() 
        
        # ✅ WRONG INPUT HANDLING
        else:
            # ✅ ĐỌC RESPONSE TEMPLATES TỪ MONGODB thay vì Data_Response.json
            try:
                data_response = data_manager.get_response_templates()
                
                # Nếu MongoDB chưa có data, fallback về file
                if not data_response:
                    print("⚠️ No templates in MongoDB, reading from file...")
                    data_response = js.load(open("data/Data_Response.json"))
            except Exception as e:
                print(f"⚠️ Error reading templates: {e}, fallback to file")
                data_response = js.load(open("data/Data_Response.json"))
            
            if self.isContinue:
                self.isContinue = False
                return data_response.get('wrong_input', {}).get('retry_process', 
                    'Sorry, please try again.')
            else:
                return data_response.get("wrong_input", {}).get("missing_object",
                    'I did not understand what you want to do.')


def pre_processing(string):
    from functools import reduce

    def compose(*func):
        def h(args):
            return reduce(lambda x,y: y(x), reversed(func), args)
        return h
    
    punctuation = ['.', ',', '?', '!', ';', '\'', '\"', '(', ')', '_', '-', '[', ']']
    redundant_words = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'from', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with', 'me' , 'I', 'he', 'she', 'it', 'we', 'them' , 'us']

    def removed_punctuation(string_x):
        removed_punctuation = list(filter(lambda x: '' if x in punctuation else x, string_x))
        removed_punctuation = "".join(removed_punctuation)
        return removed_punctuation

    def split_words(string_x):
        return list(map(lambda x: x, string_x.split()))
    
    def converted_lowercase(list_x):
        week_date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        converted_lowercase = list(map(lambda x: x.lower() if x not in week_date else x ,list_x))
        return converted_lowercase

    def filter_redundant_words(list_x):
            filter_stop_words = list(filter(lambda x: '' if x in redundant_words else x, list_x))
            return " ".join(filter_stop_words)
    
    proc_pipeline = compose(filter_redundant_words, converted_lowercase, split_words,  removed_punctuation)
    return proc_pipeline(string)