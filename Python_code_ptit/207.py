t = int (input())
lst = []
while len(lst) < t:
    str1 = input()
    lst.append(str1)
lstn = []
for s in range(len(lst)):
    lst1 = list(lst[s])
    for i in range (len(lst1)):
        if lst1[i].isalpha(): lst1[i] = ' '
    strso = ''.join(lst1)
    lstso = [int(x) for x in strso.split()]
    for k in lstso:
        lstn.append(k)
lstn.sort()

for i in lstn:
    print(i)

