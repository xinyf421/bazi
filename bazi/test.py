import datetime
import math
import ganzhi

tiangans = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhis = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

def calculateTime(tianganOfDay, time):
    tianganIndex = (2 * tianganOfDay - 1) % 10
    if time == 23 or time == 0 or time == 24:
        dizhi = dizhis[0]
        dizhiIndex = 0
    else:
        dizhiIndex = time / 2
        if dizhiIndex >= 0.5:
            dizhiIndex = math.ceil(dizhiIndex)
        else:
            dizhiIndex = round(dizhiIndex)
        dizhi = dizhis[dizhiIndex]
    return tiangans[(tianganIndex - 1 + dizhiIndex) % 10] + dizhi


def getShenChenBaZi(year, month, day, time):
    # data = ganzhi.day(year, month, day)
    data = ganzhi.day(year, month, day)
    tianganOfDay = data[2]
    tianganOfDaySymbol = tiangans.index(tianganOfDay) + 1
    ganzhiOfTime = calculateTime(tianganOfDaySymbol, time)
    return data[0] + '-' + ganzhiOfTime



#ganzhi核心代码部分


def main():
    shenchenbazi = getShenChenBaZi(2024, 1, 15, 23)
    print("你的生辰八字是: %s" % (shenchenbazi))

if __name__ == '__main__':
    main()