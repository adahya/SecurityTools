import sys, time
from WatchDog.WatchDog import DB_watcher

w = DB_watcher(folder='/var/Security/WatchDog/SCRDB/')

if len(sys.argv) == 2:
    if 'start' == sys.argv[1]:
        w.start()
    elif 'stop' == sys.argv[1]:
        w.stop()
    elif 'restart' == sys.argv[1]:
        w.restart()
    else:
        print("Unknown command")
        sys.exit(2)
    sys.exit(0)

else:
    print("usage: %s start|stop|restart" % sys.argv[0])
    sys.exit(2)