from TSSPM import TSSPM
import syslog


def loadTSSPM(file):
    xlsx = TSSPM(xlsxfile=file)
    syslog.syslog("Opening xlsx file")
    wsheet = xlsx.open()
    syslog.syslog("Start processing Data from Excel sheet")
    for row in range(2,wsheet.max_row):
        for column in "A":
            cell_name = '{}{}'. format(column, row)
            wsheet[cell_name].value
            syslog.syslog("Processed ["+ str(row-1) + " / " + str(wsheet.max_row) )
    del wsheet
    del xlsx
