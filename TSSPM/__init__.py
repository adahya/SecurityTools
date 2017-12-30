import openpyxl, syslog
from openpyxl.utils.exceptions import InvalidFileException, SheetTitleException


class TSSPM:
    def __init__(self,xlsxfile):
        self.xlsxfile = xlsxfile
        self.Sheet_Name = None
        self.worksheet = None
        self.workbook = None

    def open(self, sheet="TSSPM Report"):
        try:
            self.workbook = openpyxl.load_workbook(self.xlsxfile)
        except InvalidFileException as e:
            syslog.syslog(e.__cause__ )
            return None
        try:
            self.Sheet_Name = sheet
            self.worksheet = self.workbook.get_sheet_by_name(self.Sheet_Name)
        except SheetTitleException as e:
            syslog.syslog(e.__cause__)

        return self.worksheet

    def __del__(self):
        del self.xlsxfile
        del self.Sheet_Name
        del self.worksheet
        del self.workbook