s = input()
x, y = 0, 0
for i in s:
    if i == 'L':
        x -=1
    if i == 'R':
        x += 1
    if i == 'D':
        y -= 1
    if i == 'U':
        y += 1
print(str(x)+ ' '+ str(y))
