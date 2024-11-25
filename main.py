from models import wake_word_model as wwm
from observer import IObservable, IObserver
import threading
from ui import UI

class Main(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)
        self.wwm = observable #Should make this cleaner, just temp for now since it's the only thing  being observed.
        self.wakeWordThread = threading.Thread(target=self.wwm.detecting_gestures, daemon=True)
        self.wakeWordThread.start()

        self.ui = UI()
        self.ui.run()

    def notify(self, observable, *args, **kwargs):
        print("Observer notified..")
        self.listening()

    def listening(self):
        print("listening")


wake_word = wwm.WakeWordModel()
main = Main(wake_word)
