v = [[1,2], [2,3], [1,3]]

ans = 0
count = 0
data = []
for i in range(len(v)):
    data.append([v[i][0], 'x'])
    data.append([v[i][1], 'y'])

data.sort()

for i in range(len(data)):
    # Add 1 when a new class starts
    if data[i][1] == 'x':
        count += 1
    # delete 1 when class ends
    if data[i][1] == 'y':
        count -= 1
    # ans has total no of classes and count classes filled
    # so find max of classes filled vs total classes and update total class required
    ans = max(count, ans)

print(ans)
