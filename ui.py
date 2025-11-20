from tkinter import *
import json as js
from Response import Response
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
bot_name = "VA"
class ChatApplicationUI:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.response = Response()
        self.IsContinue = False
        

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width= 470, height= 550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text='Welcome', font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely= 0.07, relheight=0.012)

        # text widget
        """Area where we show the response"""
        self.text_widget = Text(self.window, width=18, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5, wrap=WORD)
        self.text_widget.place(relheight=0.745, relwidth=0.97, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.window)
        scrollbar.place(relx=0.97, rely=0.08, relheight=0.745)
        scrollbar.configure(command=self.text_widget.yview)
        self.text_widget['yscrollcommand'] = scrollbar.set

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # input box
        self.input_box = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.input_box.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.input_box.focus()
        self.input_box.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


    def _on_enter_pressed(self, event):
        input_msg = self.input_box.get()
        self._insert_message(input_msg, "You")
        element_list = self.response.get_list(input_msg)
        if element_list.get('verbs') == "start" and element_list.get('objects') == "pomodoro":
            data = js.load(open("data/Data_pomodoro.json"))
            duration = data['pomodoro']['duration']
            self._pomodoro_message()
            self.window.after(duration*1000, lambda: self._return_message(input_msg))
        else: 
            self._return_message(input_msg)

    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.input_box.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
            
    def _return_message(self, msg):
        if not msg:
            return
        self.input_box.delete(0,END)
        response_msg = self.response.get_response(msg)
        msg2 = f"{bot_name}: {response_msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        self.text_widget.see(END)
        
    def _pomodoro_message(self):
        self.input_box.delete(0,END)
        response_msg = "You are in a Pomodoro session now..."
        msg2 = f"{bot_name}: {response_msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        self.text_widget.see(END)
        
    
if __name__ == "__main__":
    app = ChatApplicationUI()
    app.run()
