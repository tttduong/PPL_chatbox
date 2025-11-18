from CompiledFiles.ChatGrammarParser import ChatGrammarParser
from CompiledFiles.ChatGrammarVisitor import ChatGrammarVisitor
from datetime import datetime
class ExtractorVisitor(ChatGrammarVisitor):
    def __init__(self):
        self.result = {}

    def visitExpression(self, ctx: ChatGrammarParser.ExpressionContext):
        if ctx.verbs():
            self.result["verbs"] = ctx.verbs().getText()
        if ctx.objects():
            if ctx.objects().getText() not in ["calendar", "meeting", "event", "weather", "pomodoro"]:
                self.result["objects"] = "invalid_input"
            else:
                self.result["objects"] = ctx.objects().getText()
        if ctx.time():
            self.visit(ctx.time())
        if ctx.location():
            self.result["location"] = self.visit(ctx.location())
        if ctx.query():
            self.result["query"] = self.visit(ctx.query())
        if ctx.TITLE_STRING():
            import json as js
            objects = js.load(open("data/Data_temp.json"))['objects']
            title = ctx.TITLE_STRING().getText()
            print(title)
            self.result["title"] = title.replace("\"", "").strip()
            self.result["objects"] = objects
        
        return self.result

    def visitTime(self, ctx: ChatGrammarParser.TimeContext):
        if ctx.start_time():
            start_time = self.visit(ctx.start_time())
            self.result["start_time"] = start_time
        if ctx.end_time():
            end_time = self.visit(ctx.end_time())
            self.result["end_time"] = end_time
        if ctx.today():
            self.result["date"] = datetime.today().strftime('%d/%m/%Y')
        if ctx.date():
            self.result["date"] = ctx.date().getText()
        if ctx.duration():
            duration = self.visit(ctx.duration())
            self.result["duration"] = duration
        return self.result

    def visitStart_time(self, ctx: ChatGrammarParser.Start_timeContext):
        hour = int(ctx.INT(0).getText())
        minute = int(ctx.INT(1).getText())
        if (minute >= 60) :
            minute = 'invalid_input'
        if hour >= 25 :
            hour = 'invalid_input'
        return f"{hour:02d}:{minute:02d}"
    
    def visitEnd_time(self, ctx: ChatGrammarParser.End_timeContext):
        hour = int(ctx.INT(0).getText())
        minute = int(ctx.INT(1).getText())
        if (minute >= 60) :
            minute = 'invalid_input'
        if hour >= 25 :
            hour = 'invalid_input'
        return f"{hour:02d}:{minute:02d}"
        
    def visitLocation(self, ctx: ChatGrammarParser.LocationContext):
        return ctx.getText()
    
    def visitQuery(self, ctx:ChatGrammarParser.QueryContext):
        return ctx.getText()

    def visitDuration(self, ctx: ChatGrammarParser.DurationContext):
        minute = int(ctx.INT().getText())
        return f"{minute}"