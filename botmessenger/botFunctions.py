import time


# gets the hour
def hourGetter():
    strTime = str(time.localtime())
    # print strTime
    trash, hourAndTrash = strTime.split("tm_hour=")
    # print hourAndTrash
    hour = hourAndTrash.split(", ")
    # print hour[0]
    return hour[0]


# gets the day of the year (0-365)
def dayGetter():
    strTime = str(time.localtime())
    print strTime
    trash, dayAndTrash = strTime.split("tm_yday=")
    # print hourAndTrash
    day = dayAndTrash.split(", ")
    # print hour[0]
    return day[0]


