class Solution:
    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive]+[(t, 0)for t in depart]
        events.sort()
        print(events)
        guest = 0
        for event in events:
            if event[1] == 1:
                guest += 1
            else:
                guest -= 1
            print(guest)
            if guest > K:
                return 0
        return 1


a = [13, 14, 36, 19, 44, 1, 45, 4, 48, 23, 32, 16, 37,
     44, 47, 28, 8, 47, 4, 31, 25, 48, 49, 12, 7, 8]
d = [28, 27, 61, 34, 73, 18, 50, 5, 86, 28, 34, 32, 75,
     45, 68, 65, 35, 91, 13, 76, 60, 90, 67, 22, 51, 53]
k = 23
object = Solution()
ans = object.hotel(a, d, k)
print()
print(ans)
