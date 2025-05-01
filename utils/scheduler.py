import time
import threading
import datetime
from utils.observer import IObservable
import playsound

class Reminder():
    def __init__(self, time, message):
        self.time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        self.message = message

class Timer():
    def __init__(self, duration):
        self.duration = duration
        
class Scheduler(IObservable):
    def __init__(self):
        self.observers = set()
        self.reminders = []
        self.timers = []
        self.lock = threading.Lock()
        self.alarmSoundPath = "assets/alarm.mp3"
        threading.Thread(target=self.check_timers, daemon=True).start()
        threading.Thread(target=self.check_reminders, daemon=True).start()

    def add_reminder(self, time, message):
        with self.lock:
            reminder = Reminder(time, message)
            self.reminders.append(reminder)

    def add_timer(self, duration):
        with self.lock:
            timer = Timer(duration)
            self.timers.append(timer)

    def check_reminders(self):
        while True:
            with self.lock:
                current_time = datetime.datetime.now()
                for reminder in self.reminders[:]:
                    if current_time >= reminder.time:
                        try:
                            threading.Thread(target=playsound, args=(self.alarmSoundPath,), daemon=True).start()
                        except Exception as e:
                            print(f"Error playing sound: {e}")
                        self.notify(message = reminder.message)
                        self.reminders.remove(reminder)
            time.sleep(1)

    def check_timers(self):
        while True:
            time.sleep(1)
            with self.lock:
                for timer in self.timers[:]:
                    timer.duration -= 1
                    if timer.duration <= 0:
                        threading.Thread(target=playsound, args=(self.alarmSoundPath,), daemon=True).start()
                        self.notify(timer = timer.duration)
                        self.timers.remove(timer)