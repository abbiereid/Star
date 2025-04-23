from ollama import chat

class Assistant:
    def __init__(self):
        self.model = "llama3.2"

    def recieveRequest(self, request):
        return self.preprocessRequest(request)

    def preprocessRequest(self, request):
        request= [
            {"role": "assistant", "content": "You are a helpful assistant for non-verbal users, you will be given requests that have been translated from American Sign Language, so they may be in glosses. This means that rather than grammar like How are You? It could be How you? or How you are? Please do your best to translate this to English Grammar before you respond in english please. Also please restrict the length of your response to up to 50 words. Your response should be to the user in a friendly manner."},
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