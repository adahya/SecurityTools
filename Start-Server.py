from WatchDog.WatchDog import DB_watcher

w = DB_watcher(folder='/var/Security/WatchDog/SCRDB/')
w.run()
