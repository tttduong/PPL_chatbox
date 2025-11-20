#đảm bảo rằng mọi module con (như Weather.py, Calendar.py) 
# khi được tạo ra đều có cùng các phương thức cơ bản
class Module():
    def __init__(self, list):
        self.list = list
    def take_action(self):
        print("do action base on verb and time")
    def return_response(self):
        print("return response")