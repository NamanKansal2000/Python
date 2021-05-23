s = input()
a = s[2]
f1 = f2 = False
if a not in ["A","E","I","O","U","Y"]:
    f1 = True
for i in range(len(s)-1):
    if not (s[i].isdigit() and s[i+1].isdigit()):
        continue
    if (int(s[i])+int(s[i+1]))%2 != 0:
        f2 = False
        break
    else:
        f2 = True
if f1 and f2:
    print('valid')
else:
    print('invalid')
