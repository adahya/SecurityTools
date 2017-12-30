from TSSPM import TSSPM
import syslog


def loadTSSPM(file):
    xlsx = TSSPM(xlsxfile=file)
    syslog.syslog("Opening xlsx file")
    wsheet = xlsx.open()
    for row in range(2,wsheet.max_row):
        for column in "A":
            cell_name = '{}{}'. format(column, row)
            syslog.syslog("SCR Number:" + wsheet[cell_name].value)
    del wsheet
    del xlsx