n = int(input())
counts = {}
name = []
score = []
for _ in range(n):
    inp = input()
    val = inp.split()
    name.append(val[0])
    for i in range(len(val)-1):
        score[i].append(float([val[1:]]))

for key in name:
    for val in score:
        counts[key] = val

str = input()
print(counts)
for i,lst in counts.items():
    if i == str:
        score = lst
        print(sum(score)/len(score))
    else:
        pass
