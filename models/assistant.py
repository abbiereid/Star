from ollama import chat

class Assistant:
    def __init__(self):
        self.model = "llama3.2"
        self.history = []

    def recieveRequest(self, request):
        return self.preprocessRequest(request)

    def preprocessRequest(self, request):
        preprocessed_request= [
            {
                "role": "system",
                "content": (
                "You are a helpful home assistant."
                "Requests given to you may be glosses as they have been translated from ASL,"
                "Requests may lack the letters 'J' and 'Z' as they can be difficult to translate,"
                "So, some requests may require autocorrection"
                "You are to respond in a helpful and friendly manner,"
                "Please keep your responses short and to the point, no more than 2 sentences" 
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