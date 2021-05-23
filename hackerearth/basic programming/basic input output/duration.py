t = int(input())
for _ in range(t):
    sh, sm, eh, em = map(int, input().split())
    t = (eh*60 + em) - (sh*60 + sm)
    wh = t//60
    wm = t%60
    print(str(wh) + ' '+ str(wm))
