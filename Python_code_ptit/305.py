t, l = map(int, input().split())
lst = []
while len(lst) < t:
    str1 = input()
    lst.append(str1.lower())
dic = {}
for s in range(len(lst)):
    lst1 = list(lst[s])
    for i in range (len(lst1)):
        if not lst1[i].isalpha() and not lst1[i].isalnum(): lst1[i] = ' '
    strso = ''.join(lst1)
    lstso = [x for x in strso.split()]
    for k in lstso:
        if k not in dic:
            dic[k] = 1
        else:
            dic[k]+=1
ma = 0
for i in dic:
    if dic[i] > ma: ma = dic[i]
dics = sorted(dic)
while ma > l-1 :
    for i in dics:
        if dic[i] == ma:
            print("{} {}".format(i,dic[i]))
    ma-=1
