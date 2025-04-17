from ollama import chat

class Assistant:
    def __init__(self):
        self.model = "llama3.2"

    def recieveRequest(self, request):
        self.processRequest(self.preprocessRequest(request))

    def preprocessRequest(self, request):
        request= [
            {"role": "system", "content": "You are a helpful assistant for non-verbal users, you will be given requests in ASL glosses, please translate them to English and respond in English."},
            {"role": "user", "content": request}
        ]
        self.processRequest(request)
    

    def processRequest(self, request):
        try:
            self.sendResponse(chat(self.model, request))
        except Exception as e:
            self.sendResponse(f"An error occurred: {e}")

    def sendResponse(self, response):
        print(response)