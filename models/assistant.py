from ollama import chat

class Assistant:
    def __init__(self):
        self.model = "llama3.2"

    def recieveRequest(self, request):
        return self.preprocessRequest(request)

    def preprocessRequest(self, request):
        request= [
            {"role": "assistant", "content": 
                ""},
            {"role": "user", "content": request}
        ]
        return self.processRequest(request)
    

    def processRequest(self, request):
        try:
            self.response = chat(self.model, request)
            if self.response.message.content == "":
                return "Sorry, I couldn't understand your request."
            else:
                return self.response.message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, I couldn't process your request at the moment."