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
        self.listeningState = False

        self.ui = UI()
        self.ui.run()

    def notify(self, observable, *args, **kwargs):
        print("Observer notified..")
        self.listeningState = kwargs.get('state', False)
        if self.listeningState:
            self.listening()
        else:
            self.stopListening()

    def listening(self): #This is what will call SLR4BSL service
        print("listening")
        self.ui.show_listening()

    #Stop Listening is a temp function as I have yet to implement the awareness of when a user has completed a request.
    #Needed something manual for the time being.
    def stopListening(self):
        print("Stopped listening..")


wake_word = wwm.WakeWordModel()
main = Main(wake_word)
