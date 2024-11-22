from abc import ABC, abstractmethod

class IObservable(ABC):
    def __init__(self):
        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)
    
    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.notify(self, *args, **kwargs)


class IObserver(ABC):
    def __init__(self, observable):
        observable.subscribe(self)

    @abstractmethod
    def notify(self, observable, *args, **kwargs):
        print("Observer notified..")