"""
ID: jam.cod1
LANG: PYTHON3
TASK: friday
"""
fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

n = int(fin.readline().strip())
startday = 1
nowy = 1900
m = 1
d = 1
xq = 1

endy = 1900 + n - 1


def leapornot(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False


#        Dec Jan Feb                                 Nov
months = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
leaps =  [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

days = [0] * 7

d13 = startday - 1 + 13
m = 1
endMonth = n * 12
startyear=1900

while m <= endMonth:
    days[d13 % 7] += 1
    mth = m % 12
    d13 += leaps[mth] if leapornot(m // 12 + startyear) else months[mth]
    m += 1
days.insert(0, days.pop(-1))

ans= list(map(lambda x: str(x), days))

fout.write (' '.join(ans) + '\n')
fout.close()