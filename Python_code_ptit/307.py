s=''
while True:
  try: 
    st = input() 
    s += st + " " 
  except EOFError: break

s = s.replace('!', '.')
s = s.replace('?', '.')
cau = s.split('.')
for i in cau:
  lst = i.lower().strip().split()
  print("".join(lst[:1]).title(), end = ' ')
  b = ' '.join(lst[1:])
  print(b)
