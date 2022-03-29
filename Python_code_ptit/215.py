while True:
    s = input()
    if s == "0 0 0 0":
        break
    else:
        lst = [int(x) for x in s.split()]
    count = 0
    while len(list(set(lst))) > 1:
        temp = lst[0]
        lst[0] = abs(lst[0] - lst[1])
        lst[1] = abs(lst[1] - lst[2])
        lst[2] = abs(lst[2] - lst[3])
        lst[3] = abs(lst[3] - temp)
        count += 1
    print(count)