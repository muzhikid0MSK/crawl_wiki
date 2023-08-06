import re


def validatetitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    if new_title.endswith(" "):
        new_title = new_title[:-1]
    return new_title
