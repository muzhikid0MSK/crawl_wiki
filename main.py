from Executors import Executor
from Services.WikiService import WikiService
from Services.ReadExcelService import ReadExcelService
from Utils.WalkUtils import *


# 只取needed里面的
def file_filter(origin_list, needed: list):
    if needed is [] or needed is None:
        return origin_list
    filt_res = []
    for file in origin_list:
        for n in needed:
            flag = False
            if n in file:
                filt_res.append(file)
                flag = True
            if flag:
                break
    return filt_res


def run_wiki_service():
    root_dir_path = "C:\\Users\\meish\\Documents\\WeChat Files\\wxid_9qctubkcyc522\\FileStorage\\File\\2023-08\\ports"
    file_list = walk_files(root_dir_path)

    # filter = ["西班牙港口", "韩国港口"]
    # file_list = file_filter(file_list,filter)
    for file in file_list:
        read_excel_service = ReadExcelService(file)
        wiki_service = WikiService(read_excel_service.work_book, 5, file.split("\\")[-1].replace(".xlsx", ""),
                                   person="易炳艳")
        options = {
            "region": "en",
            "multi-thread": True,
        }
        wiki_service.run(**options)


#
# def rename_ch_to_en():


if __name__ == "__main__":
    run_wiki_service()
