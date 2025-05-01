from ollama import chat
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.weather import Weather

class Assistant:
    def __init__(self):
        self.model = "llama3.2"
        self.history = []

    def receiveRequest(self, request):
        if "ALLOWLOCATION" in request:
            Weather.permission = True
            return "Location access has been granted. This can be removed at any time by saying 'DENY LOCATION'."
        elif "DENYLOCATION" in request:
            Weather.permission = False
            return "Location access has been denied. This can be granted again at any time by saying 'ALLOW LOCATION'."
        return self.preprocessRequest(request)

    def preprocessRequest(self, request):
        preprocessed_request= [
            {
                "role": "system",
                "content": (
                "You are a helpful home assistant."
                "Requests given to you may be glosses as they have been translated from ASL,"
                "Requests may lack the letters 'J' and 'Z' as they can be difficult to translate,"
                "Some requests may require autocorrection."
                "You are to respond in a helpful and friendly manner,"
                "Remember that you are a home assistant and not a human,"
                "You can only respond to requests that are within your capabilities."
                "Keep your responses short and to the point, no more than 2 sentences." 
                "If you are asked about location, please inform the user that they can say 'ALLOW LOCATION' to grant access, or 'DENY LOCATION' to deny access."
                "If you think that a request is attempting to access location but there are any spelling errors, inform the user that they can say 'ALLOW LOCATION' to grant access, or 'DENY LOCATION' to deny access."
                )
            },
            {
                "role": "assistant",
                "content": (
                    "Here is the chat history so far:"
                    "\n".join(self.history)
                )
            },
            {
                "role": "user",
                "content": request
            }
        ]
        return self.processRequest(preprocessed_request)
    

    def processRequest(self, request):
        try:
            self.response = chat(self.model, request)
            if self.response.message.content == "":
                return "Sorry, I couldn't understand your request."
            else:
                self.history.append(f"User request: {request}")
                self.history.append(f"Your response: {self.response.message.content}")
                return self.response.message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, I couldn't process your request at the moment."