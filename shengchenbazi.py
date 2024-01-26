import datetime
import math

tiangans = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhis = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
shengxiaos = ["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]

CHINESE_1990_2100 = [
    51397716,54792469,205819985,55641108,55656721,206770449,51450948,54608977,207688017,51397716,
    219177285,54792273,55641105,222610449,54858000,55645252,220483908,54595909,205589781,51396885,
    54792261,219451461,51659793,51663120,219366673,50611476,54595861,207684693,51396885,206594324,
    55644228,55854097,206685249,51463249,50611476,218895444,54592596,222366801,55591185,55644228,
    222638148,54858001,51450948,219353413,50598225,54592593,224461893,54804753,219433233,51662916,
    54858001,205833489,51401028,54792517,206311701,51446853,219219524,55853329,51659844,219243588,
    54805777,51397908,219300948,54792469,51446804,223937556,55656721,205854993,51450948,54596689,
    205623633,51397713,54792273,222695505,55641105,222578193,54858000,54858820,218394948,54595909,
    51396933,219300117,54792261,219418725,51659793,51663120,219243792,54805780,54595861,205620309,
    51396885,51646533,207163460,55854097,206640657,51463248,54805780,218403921,54592596,55591188,
    222707985,55644228,55657489,207950097,51450948,219224389,50598225,54592593,222397509,54804753,
    54857796,219563076,54808849,205800849,51397956,54792517,205795605,51446853,54804741,206979345,
    51659844,54808849,207701265,51397908,219178068,54792276,55641108,223446036,55644421,51463236,
    207164484,54596689,205590873,51397713,54792273,222572613,55641105,55644420,222662928,54858052,
    51450961,207688005,51396933,219171093,54792261,54805521,219464721,51663108,54808900,206325012,
    54592789,205588053,51396885,51646533,206647364,55854097,51659844,219354192,54805588,54592596,
    222889044,55591188,222578961,55644228,55657489,205885713,51450948,54793297,205918545,51446865,
    219219525,54804753,54857796,219440196,54808849,51450180,219301188,54792517,51446853,219743253,
    51659013,206838021,51659844,54808849,205636881,51397908,54792469,205918292,55640340,223413780,
    55644420,55657540,206648388,51450961,51397716,219300177,54789201,55640337,224723985,55644420,
]

CHINESE_60= [
    '0000','0101','0202','0303','0404','0505','0606','0707','0808','0909','0010','0111',
    '0200','0301','0402','0503','0604','0705','0806','0907','0008','0109','0210','0311',
    '0400','0501','0602','0703','0804','0905','0006','0107','0208','0309','0410','0511',
    '0600','0701','0802','0903','0004','0105','0206','0307','0408','0509','0610','0711',
    '0800','0901','0002','0103','0204','0305','0406','0507','0608','0709','0810','0911',
]

CHANGE_1990_2100_24 =  [
    485536035763181,489951330300910,491395512218606,561397770413033,485536035763182,489951263192046,
    491395512218606,561397770347497,485536035763181,489951263192046,491395512218606,561397770413033,
    467943782609901,485536036811758,491119561356270,491029026238425,467943581279209,485536036811757,
    491119561356270,491029026238425,467939286311913,485536036811757,489951330251758,491029026238425,
    467939286311913,485536035763181,489951330300910,491029009460889,467939282052073,485536035763181,
    489951330300910,491029026238105,467939282052073,485536035763181,489951263192046,491029009460889,
    467939282052073,485536035763181,489951263192046,491029009460889,467939282052073,485536035763181,
    489951263192046,491027935719065,467939282055129,467943849714669,485536036811758,490753057549977,
    397570537877465,467939286246381,485536036811758,490753057549977,397570537877465,467939286311913,
    485536035763181,490684338073241,397570537877465,467939282052073,485536035763181,489584826429081,
    397570521099929,467939282052073,485536035763181,489584826429081,397570521099929,467939282052073,
    485536035763181,489584759320217,397570521099929,467939282052073,485536035765997,489584759320217,
    397569447358105,467939282052073,485536035759085,489567579451033,397569447095961,467939282055145,
    485535767323629,489567579451033,397569447095961,467939282055129,467939286311917,485169531891353,
    397294569189017,397570537877465,467939282117609,485169531891352,397225849695897,397570521100249,
    467939282052073,485169532939928,396126338068121,397570521099929,467939282052073,485169531891352,
    396126270959257,397570521099929,467939282052073,485169531891352,396126270959257,397570521099929,
    467939282052073,485169531891352,396126270959257,397569447095961,467939282052073,485169531887256,
    396109091090073,397569447095961,467939282055145,485169263451800,396109090041497,397569447095961,
    467939282055129,467572782440088,391711043530393,397294569189017,397570521100249,467572778180248,
    391711043530392,397225849695897,397570521100249,467572778180244,391711043530392,396126270959257,
    397570521099929,467572778180244,391711043530392,396126270959257,397570521099929,467572778180244,
    391711043530392,396126270959257,397569447095961,467572778180244,391711043530392,396126270959257,
    397569447095961,466473266552468,391710775090840,396109091090073,397569447095961,467572778179220,
    391706480123544,396109090041497,397569447095961,467572761401988,374114289819288,391711043530393,
    397225849695897,379611831179908,374114289819288,391711043530393,397208602717849,397204017224324,
    374114289819284,391711043530392,397225782587033,397204017224004,374114289819284,391711043530392,
    396126270959257,397204017224004,374114289819284,391711043530392,396126270959257,397202943220036,
    374114289819284,391710775029400,396126270959257,397202943220036,374114289818260,391710775090840,
    396109090041497,397202943220036,374114289818260,391706475929240,396109090041497,397202943220036,
    375213784668804,391706475863704,391711043530393,397134223726916,303745528601220,374114289819288,
    391711043530393,397134156618052,303745528846724,374114289819284,391711043530392,397134156618052,
    303745528863044,374114289819284,391711043530392,396034644990276,303745528600900,374114289819284,
    391711043530392,396126270959257,
]

def calculateTime(tianganOfDay, time):
    tianganIndex = (2 * tianganOfDay - 1) % 10
    if time == 23 or time == 0 or time == 24:
        dizhi = dizhis[0]
        dizhiIndex = 0
    else:
        dizhiIndex = math.ceil(time / 2)
        dizhi = dizhis[dizhiIndex]
    return tiangans[(tianganIndex - 1 + dizhiIndex) % 10] + dizhi

def getShenChenBaZi(year, month, day, time):
    data = dday(year, month, day)
    tianganOfDay = data[2]
    tianganOfDaySymbol = tiangans.index(tianganOfDay) + 1
    ganzhiOfTime = calculateTime(tianganOfDaySymbol, time)
    return data[0] + '-' + ganzhiOfTime

def dday(english_year, english_month, english_day):
    # 旧历的计算
    chinese_years_days = helper_days_list()
    english_days = (datetime.date(english_year, english_month, english_day) - datetime.date(1901, 1, 1)).days # 获取输入日期的天数
    if english_days < 50:
        d49 = day_49(english_year, english_month, english_day)
        return d49
    chinese_year_list = helper_year_data_find(english_days, chinese_years_days)  # 获得年位置 [33271, 91, 1992, 16]

    change_dict = {'00': 29, '01': 30, '10': 29, '11': 30, }
    a = bin(CHINESE_1990_2100[chinese_year_list[1]])[2:]
    b = [a[i:i + 2] for i in range(0, len(a), 2)][2:] # 二进制列表
    c = [change_dict.get(x, x) for x in b]  # 十进制列表
    d = [sum(c[0:i]) for i in range(len(c))] # 月份的天数
    chinese_month_list = helper_month_data_find(chinese_year_list[3], d)  # 获得月位置 [0, 0, 1, 17]
    chinese_month_list_2 = chinese_month_list[2]
    if len(b) == 13:
        r = [(i, b.index(i)) for i in b if i in ('10', '11')][0]
        chinese_month_list_2 = chinese_month_list_2 - 1 if chinese_month_list_2 > r[1] else chinese_month_list_2

    # 天干地支的计算
    chinese_years_days_60 = helper_days_60_list()
    chinese_year_list = helper_year_60_data_find(english_days, chinese_years_days_60)
    year_60_list = CHINESE_60 * 5
    year_60_list = year_60_list[37:37 + 200]  # 生成年干支列表

    e = bin(CHANGE_1990_2100_24[chinese_year_list[1]])[3:]  # 解析24气节的数据
    f = [e[i:i + 2] for i in range(0, len(e), 2)]  # 去除保留数值
    g = [f[i] for i in range(2, len(f), 2)]
    a1 = {'00': '2', '01': '3', '10': '4', '11': '5', }
    a2 = {'00': '4', '01': '5', '10': '6', '11': '7', }
    a3 = {'00': '9', '01': '6', '10': '7', '11': '8', }
    g_list = [a1[g[0]], a2[g[1]], a2[g[2]], a2[g[3]], a2[g[4]], a3[g[5]], a3[g[6]], a3[g[7]], a3[g[8]], a3[g[9]],
              a3[g[10]], ]  # 转换为１０进制的列表

    e2 = bin(CHANGE_1990_2100_24[chinese_year_list[1] + 1])[3:]  # 获取向前一年的u"小寒",u"大寒"
    f2 = [e2[i:i + 2] for i in range(0, len(e2), 2)]
    g2 = [f2[i] for i in range(0, len(f2), 2)]
    g_list = g_list + [a2[g2[0]]]  # 生成完整的10进制列表

    g_list_new = []
    for v in range(11):
        v_day = datetime.date(chinese_year_list[2], 2 + v, int(g_list[v])) - datetime.date(chinese_year_list[2], 2,
                                                                                           int(g_list[0]))
        g_list_new.append(v_day.days)
    v_day_2 = datetime.date(chinese_year_list[2] + 1, 1, int(g_list[11])) - datetime.date(chinese_year_list[2], 2,
                                                                                          int(g_list[0]))
    g_list_new.append(v_day_2.days)  # 生成月干支天数，数据列表
    chinese_month_days_60 = helper_month_60_data_find(chinese_year_list[3], g_list_new)  # 获得月干支位置[60, 2, 3, 1]

    year_value_key = int(year_60_list[chinese_year_list[1]][0:2])  # 年干
    year_value = year_value_key if year_value_key <= 4 else year_value_key - 5  # 通过年干支定位月干支列表
    v1 = tiangans *3
    month_value = 2 + (year_value * 2)  # 获取开始位置的公式
    v2 = v1[month_value:month_value + 12]  # 生成月干
    v3 = dizhis[2:] + dizhis[0:2]  # 生成月支，因为一月为u"寅"

    v4 = datetime.date(english_year, english_month, english_day) - datetime.date(1901, 2, 15)  # 日干支
    v5 = v4.days % 60
    f1 = str(english_year) + '-' + str(english_month) + '-' + str(english_day)
    f2 = str(chinese_year_list[2]) + '-' + str(chinese_month_list_2) + '-' + str(chinese_month_list[3])
    f3 = tiangans[int(year_60_list[chinese_year_list[1]][0:2])] + dizhis[
        int(year_60_list[chinese_year_list[1]][2:4])] + '-' + v2[chinese_month_days_60[1]] + v3[
             chinese_month_days_60[1]] + '-' + tiangans[int(CHINESE_60[v5][0:2])] + dizhis[
             int(CHINESE_60[v5][2:4])]
    f4 = shengxiaos[int(year_60_list[chinese_year_list[1]][2:4])]  # 生肖
    f5 = tiangans[int(CHINESE_60[v5][0:2])]  # 日的天干
    # print(u'输入:[' + f1 + u']; 输出:[' + f2 + u']; 天干地支:[' + f3 + u']; 生肖:[' + f4 + ']')
    return [f3, f4, f5]

def helper_days_list():
    chinese_years_data =49
    chinese_years_list = [49]
    change_dict = {'00':29, '01':30, '10':29,'11':30,}

    for i in CHINESE_1990_2100:
        a = bin(i)
        b = [ a[i:i+2] for i in range(0, len(a),2)][2:] #转为二进制的列表
        c = sum([ int(change_dict[x]) if x in change_dict else int(x) for x in b]) #转为十进制的列表
        chinese_years_data = chinese_years_data + c #得出年初的天数
        chinese_years_list.append(chinese_years_data) #添加进列表
    return chinese_years_list #返回列表

def day_49(english_year, english_month, english_day):
    english_days = datetime.date(english_year, english_month, english_day) - datetime.date(1901, 1, 1)
    english_days = english_days.days
    chinese_year = '1900'
    chinese_month = '12' if english_days > 18 else '11'
    chinese_day = english_days + 11 if chinese_month == '11' else english_days - 18

    chinese_year_60 = '0600' if english_days < 34 else '0701'  # 庚子 '辛丑'
    chinese_month_60 = u'戊子' if english_days < 6 else (u'乙丑' if english_days < 34 else u'庚寅')

    v4 = datetime.date(english_year, english_month, english_day) - datetime.date(1900, 12, 17)  # 日干支
    v5 = v4.days % 60

    f1 = str(english_year) + '-' + str(english_month) + '-' + str(english_day)
    f2 = chinese_year + '-' + chinese_month + '-' + str(chinese_day)
    a = tiangans[int(chinese_year_60[0:2])] + dizhis[int(chinese_year_60[2:4])]
    c = tiangans[int(CHINESE_60[v5][0:2])] + dizhis[int(CHINESE_60[v5][2:4])]

    f3 = a + '-' + chinese_month_60 + '-' + c
    f4 = shengxiaos[int(CHINESE_60[v5][2:4])]
    return [f1, f2, f3, f4]

def helper_month_data_find(value,li):
    chinese_month_data_find = [ (i,li.index(i))  for i in li if i <= value ][-1]
    return [chinese_month_data_find[0],chinese_month_data_find[1],1+ chinese_month_data_find[1],value-chinese_month_data_find[0]+1]

def helper_year_data_find(value,li):
    chinese_year_data_find = [ (i,li.index(i))  for i in li if i <= value ][-1]
    return [chinese_year_data_find [0],chinese_year_data_find [1],1901+chinese_year_data_find [1],value-chinese_year_data_find[0]]

def helper_days_60_list():
    chinese_years_data = 1901
    chinese_years_list = []
    change_dict = {'00': '2', '01': '3', '10': '4', '11': '5', }

    for t in range(len(CHANGE_1990_2100_24)):
        a = bin(CHANGE_1990_2100_24[t])
        a = a[3:]
        b = [a[i:i + 2] for i in range(0, len(a), 2)][2]  # 转为二进制的列表
        c = int(change_dict[b])  # 立春的天数
        english_days = datetime.date(chinese_years_data + t, 2, c) - datetime.date(1901, 1, 1)
        chinese_years_list.append(english_days.days)  # 添加进列表

    return chinese_years_list  # 返回列表

def helper_month_60_data_find(value, li):
    chinese_month_data_find = [(i, li.index(i)) for i in li if i <= value][-1]
    return [chinese_month_data_find[0], chinese_month_data_find[1], 1 + chinese_month_data_find[1],
            value - chinese_month_data_find[0] + 1]

def helper_year_60_data_find(value, li):
    chinese_year_data_find = [(i, li.index(i)) for i in li if i <= value][-1]
    return [chinese_year_data_find[0], chinese_year_data_find[1], 1901 + chinese_year_data_find[1],
            value - chinese_year_data_find[0]]

def main():
    # shenchenbazi = getShenChenBaZi(1988, 6, 9, 5)
    year, month, day, hour = map(int, input("请输入出生年月日和时间（例如：1988 6 9 5）：").split())
    shenchenbazi = getShenChenBaZi(year, month, day, hour)
    print("你的生辰八字是: %s" % (shenchenbazi))

if __name__ == '__main__':
    main()