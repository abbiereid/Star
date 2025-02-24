from models import wake_word_model as wwm
from models import bsl_translator as bslt
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
        self.listeningAnimationThread = None
        self.translatingThread = None

        self.translator = bslt.SignLanguageRecogniser()

        self.ui = UI()
        self.ui.run()

    def notify(self, observable, *args, **kwargs):
        self.listeningState = kwargs.get('state', False)
        if self.listeningState:
            self.listening()
        else:
            self.stopListening()

    def listening(self):
        if self.listeningAnimationThread is None:
            self.listeningAnimationThread = threading.Thread(target=self.ui.show_listening, daemon=True)
            self.listeningAnimationThread.start()

        if self.translatingThread is None:
            self.translatingThread = threading.Thread(target=self.translator.record_request(), daemon=True)
            self.translatingThread.start()

    #Stop Listening is a temp function as I have yet to implement the awareness of when a user has completed a request.
    #Needed something manual for the time being.
    def stopListening(self):
        self.ui.stop_listening()
        self.translator.stop_recording()

        if self.listeningAnimationThread is not None:
            self.listeningAnimationThread.join()
            self.listeningAnimationThread = None

        if self.translatingThread is not None:
            self.translatingThread.join()
            self.translatingThread = None

wake_word = wwm.WakeWordModel()
main = Main(wake_word)
