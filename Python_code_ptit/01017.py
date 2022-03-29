t = int(input())
while t:
    st = input()
    n = len(st)
    st += ' '
    str1 = ''
    ind = -1
    for i in range(n):
        if st[i] != st[i+1]:
            str1 += str(i-ind) + st[i]
            ind = i
    print (str1)
    t -= 1