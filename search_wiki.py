from Executors import Executor
from Services.WikiService import WikiService
from Services.ReadExcelService import ReadExcelService
from Utils.WalkUtils import *
import multiprocessing


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


def load_chrome_webdriver(thread_num, browsers: list, browsers_locks: list):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from threading import Lock
    webservice = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
    print("加载浏览器驱动 -- 开始 -- ")
    for i in range(thread_num):
        chrome_options = Options()
        # 设置chrome浏览器无界面模式
        chrome_options.add_argument('--headless')
        # 另存为mhtml模式
        chrome_options.add_argument('--save-page-as-mhtml')
        browsers.append(webdriver.Chrome(chrome_options, webservice))

        browsers_locks.append(Lock())
    print("加载浏览器驱动 -- 结束 -- ")
    print("")


def run_wiki_service():
    root_dir_path = "C:\\Users\\meish\\Documents\\WeChat Files\\wxid_9qctubkcyc522\\FileStorage\\File\\2023-08\\xlsx(1)\\xlsx"
    # root_dir_path = "C:\\Users\\meish\\Documents\\WeChat Files\\wxid_9qctubkcyc522\\FileStorage\\File\\2023-08\\ports"
    file_list = walk_files(root_dir_path)

    # filter = ["西班牙港口", "韩国港口"]
    # file_list = file_filter(file_list,filter)
    browsers = []
    browsers_locks = []

    load_chrome_webdriver(multiprocessing.cpu_count() - 1, browsers, browsers_locks)

    for file in file_list:
        read_excel_service = ReadExcelService(file)
        wiki_service = WikiService(read_excel_service.work_book, browsers, browsers_locks,
                                   file.split("\\")[-1].replace(".xlsx", ""),
                                   person="某某")
        options = {
            "multi-thread": True,
        }
        wiki_service.run(**options)


#
# def rename_ch_to_en():


if __name__ == "__main__":
    run_wiki_service()
