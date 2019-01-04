import generateImage as ImageGen
import generateNewYearImage as ImageGenNY
import instagramCalls as insta
import time
import calendar
import datetime

def main():
    todayDate = datetime.datetime.fromtimestamp(time.time()).date()
    lastUpdate, lastPercent = insta.getLastUploadDate()
    if lastUpdate < todayDate and lastPercent < getProgressPercent():
        ImageGen.generateAndSave(getProgressPercent())
    elif lastUpdate < todayDate and lastPercent == 100 and getProgressPercent() == 0:
        # Happy New Year :)
        ImageGenNY.generateAndSave(getProgressPercent())


def getProgressPercent():
    today = datetime.datetime.now()
    if(calendar.isleap(today.year)):
        daysInMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        totalDays = 366
    else:
        daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        totalDays = 365

    daysCompleted = 0
    for i in range (0, today.month - 1):
        daysCompleted += daysInMonths[i]
    daysCompleted += int(today.day)

    progressPercent = int((daysCompleted/totalDays)*100)
    return progressPercent

main()