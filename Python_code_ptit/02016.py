from enum import unique


t = int(input())
for i in range(t):
    n = int(input())
    dict = {}
    arr = [int(s) for s in input().split()]
    for num in arr:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] = dict.get(num) + 1
    for num in dict:
        if dict.get(num) > n // 2:
            print(num)
            break
    else:
        print("NO")