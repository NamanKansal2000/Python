class Solution:
    def hotel(self, arrive, depart, K):
        n = len(arrive)
        sch = []
        curr, max_ = 0, 0
        # values assigned will change based on
        # wether we consider derpart first or arrival first
        # in case of clash
        for i in range(n):
            sch.append([arrive[i], 1])
            sch.append([depart[i],0])
        sch.sort()
        for i in range(len(sch)):
            if sch[i][1] == 1:
                curr += 1
                max_ = max(curr, max_)
            else:
                curr -= 1
        return K >= max_

A = [1, 3, 5]
B = [2, 6, 8]
C = 1
s = Solution()
print(s.hotel(A,B,C))
