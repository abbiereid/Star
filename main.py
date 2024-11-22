from models import wake_word_model as wwm
from observer import IObservable, IObserver
import threading
from ui import UI

class Main(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("Observer notified..")
        self.listening()

    def listening(self):
        print("listening")


wwm = wwm.WakeWordModel()
ui = UI()
main = Main(wwm)

wakeWordThread = threading.Thread(target=wwm.detecting_gestures, daemon=True)
wakeWordThread.start()

ui.run()

