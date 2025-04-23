from models import wake_word_model as wwm
from models import sign_language_recognition as slt
from utils.observer import IObservable, IObserver
import threading
from utils.ui import UI
from utils.textTospeech import TextToSpeech

class Main(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)
        self.wwm = observable #Should make this cleaner, just temp for now since it's the only thing  being observed.
        self.wakeWordThread = threading.Thread(target=self.wwm.detecting_gestures, daemon=True)
        self.wakeWordThread.start()
        self.listeningState = False
        self.listeningAnimationThread = None
        self.translatingThread = None
        self.responseAnimationThread = None
        self.responseSpeechThread = None

        self.translator = slt.SignLanguageRecogniser()

        self.speech = TextToSpeech()

        self.ui = UI()
        self.ui.run()

    def notify(self, observable, *args, **kwargs):
        self.listeningState = kwargs.get('state', False)
        if self.listeningState:
            self.listening()
        else:
            if self.listeningAnimationThread is not None and self.translatingThread is not None:
                self.stopListening()

    def listening(self):
        if self.responseAnimationThread is not None:
            self.responseAnimationThread.join()
            self.responseAnimationThread = None

        if self.responseSpeechThread is not None:
            self.responseSpeechThread.join()
            self.responseSpeechThread = None

        if self.listeningAnimationThread is None:
            self.listeningAnimationThread = threading.Thread(target=self.ui.show_listening, daemon=True)
            self.listeningAnimationThread.start()

        if self.translatingThread is None:
            self.translatingThread = threading.Thread(target=self.translator.record_request, daemon=True)
            self.translatingThread.start()

    #Stop Listening is a temp function as I have yet to implement the awareness of when a user has completed a request.
    #Needed something manual for the time being.
    def stopListening(self):
        self.ui.stop_listening()
        self.response = self.translator.stop_recording()

        self.listeningAnimationThread.join()
        self.listeningAnimationThread = None

        self.translatingThread.join()
        self.translatingThread = None

        self.showResponse()

    def showResponse(self):
        self.responseAnimationThread = threading.Thread(target=self.ui.show_response, args=(self.response,), daemon=True)
        self.responseAnimationThread.start()

        self.responseSpeechThread = threading.Thread(target=self.speech.speak, args=(self.response,), daemon=True)
        self.responseSpeechThread.start()

wake_word = wwm.WakeWordModel()
main = Main(wake_word)