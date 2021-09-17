"""
ID: jam.cod1
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

n = int(fin.readline().strip())
namelist = []
for i in range(n):
    a = fin.readline().strip()
    namelist.append([a, 0])
    dicnamelist = dict(namelist)
for i in range(n):
    gname = fin.readline().strip()
    allmoney, giveren = fin.readline().strip().split(' ')

    allmoney = int(allmoney)
    giveren = int(giveren)
    dicnamelist[gname] = dicnamelist[gname] - allmoney
    if giveren == 0:
        everyren = 0
        shen = 0
    else:
        everyren = allmoney // giveren
        shen = allmoney % giveren
    dicnamelist[gname] = dicnamelist[gname] + shen
    for i in range(giveren):
        shouren = fin.readline().strip()
        nowmoney = dicnamelist[shouren]
        nowmoney = nowmoney + everyren
        dicnamelist[shouren] = nowmoney
for i in dicnamelist:
    ans = "{} {}".format(i, dicnamelist[i])
    fout.write(ans + '\n')
fout.close()