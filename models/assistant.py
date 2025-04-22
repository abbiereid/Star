from ollama import chat

class Assistant:
    def __init__(self):
        self.model = "llama3.2"

    def recieveRequest(self, request):
        return self.processRequest(self.preprocessRequest(request))

    def preprocessRequest(self, request):
        request= [
            {"role": "system", "content": "You are a helpful assistant for non-verbal users, you will be given requests in ASL glosses, please translate them to English and respond in English."},
            {"role": "user", "content": request}
        ]
        self.processRequest(request)
    

    def processRequest(self, request):
        try:
            return chat(self.model, request)
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, I couldn't process your request at the moment."