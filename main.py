from models import wake_word_model as wwm
from observer import IObservable, IObserver

class Main(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        self.listening

    def listening():
        print("listening")