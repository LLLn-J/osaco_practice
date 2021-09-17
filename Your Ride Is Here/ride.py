"""
ID: jam.cod1
LANG: PYTHON3
TASK: ride
"""
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

cj1 = 1
cj2 = 1

a = fin.readlines()  # .split()

for c in a[0].strip():
    cs = ord(c) - ord('A') + 1
    cj1 = cs * cj1
for c in a[1].strip():
    cs = ord(c) - ord('A') + 1
    cj2 = cs * cj2
if cj1 % 47 == cj2 % 47:
    ans = 'GO'
else:
    ans = 'STAY'

fout.write(ans + '\n')
fout.close()
