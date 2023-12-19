import time


class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    PINK = '\033[95m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEFAULT = '\033[0m'


def now(): # function returns current time in a list
    result = []
    now = time.localtime(time.time())
    if len(str(now.tm_hour)) < 2:
        result.append("0" + str(now.tm_hour))
    else:
        result.append(str(now.tm_hour))
    if len(str(now.tm_min)) < 2:
        result.append("0" + str(now.tm_min))
    else:
        result.append(str(now.tm_min))
    if len(str(now.tm_sec)) < 2:
        result.append("0" + str(now.tm_sec))
    else:
        result.append(str(now.tm_sec))
    return result


def time_print():
    time_list = now()
    print("<" + time_list[0] + ":" + time_list[1] + ":" + time_list[2] + ">")


def time_print(text):
    time_list = now()
    print("<" + time_list[0] + ":" + time_list[1] + ":" + time_list[2] + "> " + text)


# def time_print(text, color):
#     time_list = now()
#     print("<" + time_list[0] + ":" + time_list[1] + ":" + time_list[2] + "> " + text) # todo: add coments and complete this function