def khong(s):
    point = -1
    for i in range(len(s)):
        if int(s[i]) != 0:
            point = i
            break
    tmp = ""
    for i in range(point, len(s)):
        tmp += s[i]
    return tmp

def Sm(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 < n2:
        return True
    if n1 > n2:
        return False
    
    for i in range(n1):
        if s1[i] < s2[i]:
            return True
        elif s1[i] > s2[i]:
            return False

    return False

def sb(s1, s2):
    if Sm(s1, s2):
        tmpp = s1
        s1 = s2
        s2 = tmpp

    tmpString = ""
    n1 = len(s1)
    n2 = len(s2)

    s1 = s1[::-1]
    s2 = s2[::-1]

    tmp = 0

    for i in range(n2):
        sub = ((ord(s1[i]) - ord('0')) - (ord(s2[i]) - ord('0')) - tmp)

        if sub < 0:
            sub += 10
            tmp = 1
        else:
            tmp = 0
        tmpString += str(sub)

    for i in range(n2, n1):
        sub = ((ord(s1[i]) - ord('0')) - tmp)
        if sub < 0:
            sub += 10
            tmp = 1
        else:
            tmp = 0
        tmpString += str(sub)
    tmpString = tmpString[::-1]
    
    if set(tmpString) == {'0'}:
        return "0"
    else:
        tmpString = khong(tmpString)
        return tmpString

s1 = input()
if set(s1) == {'0'}:
    s1 = "0"
else:
    s1 = khong(s1)

s2 = input()
if set(s2) == {'0'}:
    s2 = "0"
else:
    s2 = khong(s2)
s3 = sb(s1, s2)
if Sm(s1, s2) and (set(s1) != {'0'} or set(s2) != {'0'}):
    s3 = '-' + s3
print(s3)