import geocoder
import python_weather

class Weather:
    def __init__(self):
        Weather.permission = False
        self.location = None
    
    async def get_users_weather(self):
        if Weather.permission:
            if self.location == None:
                self.get_location()
            return await self.get_weather(self.location)
        else:
            return "Ask Star to 'allow location' for weather details."
        
    async def get_weather(self, location):
            async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
                weather = await client.get(location.city)
                return location.city + ", " + str(weather.temperature) + "°C , " + weather.description

    def get_location(self):
        try:
            self.location = geocoder.ip('me')
        except Exception as e:
            print(f"Error getting location: {e}")
            return 'Error unable to detect location'

