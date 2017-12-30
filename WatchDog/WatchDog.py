import time, syslog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_deleted(event):
        if event.is_directory:
            return None
        else:
            syslog.syslog("Received event %s for the file %s." % (event.event_type, event.src_path))

    @staticmethod
    def on_moved(event):
        if event.is_directory:
            return None
        syslog.syslog("Received event %s for the file %s." % (event.event_type, event.src_path))


    @staticmethod
    def on_modified(event):
        if event.is_directory:
            return None
        syslog.syslog("Received event %s for the file %s." % (event.event_type, event.src_path))


class DB_watcher:

    def __init__(self, folder):
        self.observer = Observer()
        self.DIRECTORY_TO_WATCH = folder

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(30)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

