from transformers import AutoTokenizer, AutoModelForCausalLM

class Assistant:
    def __init__(self):
        self.path = "./llama-3.3-model"
        self.tokenizer = AutoTokenizer.from_pretrained(self.path)
        self.model = AutoModelForCausalLM.from_pretrained(self.path)

    def receive_request(self, request):
        pass

    def process_request(self, request):
        pass

    def send_response(self, response):
        pass