
class Weather:
    def __init__(self):
        self.permission = False
        self.location = None
    
    def get_weather(self, location):
        if self.location == None:
            self.get_location()
    
    def get_location(self):
        if self.permission:
            pass
        else:
            pass