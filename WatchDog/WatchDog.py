import time, syslog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Daemon import daemon
from TSSPM.TSSPM import loadTSSPM


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
        loadTSSPM(event.src_path)



class DB_watcher(daemon):

    def __init__(self, folder, pidfile='/Security/var/proc/watchdog/TSSPM/pidfile'):
        daemon.__init__(self,pidfile=pidfile)
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

