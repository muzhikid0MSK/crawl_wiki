from Services.Service import Service
import openpyxl


class ReadExcelService(Service):
    def __init__(self, file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = file_path
        self.work_book = None
        self.work_sheet = None
        self.work_sheet_name = kwargs.get("work_sheet", None)
        self.__pre()

    def __pre(self):
        self.work_book = openpyxl.load_workbook(self.file_path)
        if self.work_sheet_name is None:
            self.work_sheet = self.work_book.active

        else:
            self.work_sheet = self.work_book.get_sheet_by_name(self.work_sheet_name)