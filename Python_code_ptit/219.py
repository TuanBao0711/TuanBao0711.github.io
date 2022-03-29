from enum import unique

n, t = map(int,input().split())

lst = []
while len(lst) < n:
    kks = [int(s) for s in input().split()]
    lst += kks
lst.sort()
dic = {}
for num in lst:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] = dic.get(num) + 1
kq = 0
maxx = 0
for num in dic:
    if dic.get(num) > maxx:
        kq = num
        maxx = dic.get(num) 
ma = 0
count = 0
for num in dic:
    if dic.get(num) == maxx:
        dic[num] = -1
        count+=1

for num in dic:
    if dic.get(num) > ma:
        kq = num
        ma = dic.get(num)
if count == len(dic):
    print("NONE")
else:
    print(kq)