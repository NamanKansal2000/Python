def num_rooms_req(arr, dept, k):
    sch = []
    for i in range(len(arr)):
        sch.append([arr[i], 'a'])
    for i in range(len(dept)):
        sch.append([dept[i], 'd'])

    sch.sort()
    hotel = curr_hotel = 0
    for i in range(len(sch)):
        if sch[i][1] == 'a':
            curr_hotel += 1
        if sch[i][1] == 'd':
            curr_hotel -= 1

        hotel = max(hotel, curr_hotel)
        if hotel > k:
            return False

    print(hotel)
    return 0

arr = [1,3,5,6,10]
dept = [2,6,8,9,11]
k = 1
print(num_rooms_req(arr, dept,k))
