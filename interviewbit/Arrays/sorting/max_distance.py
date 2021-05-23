class Solution:
    def maximumGap(self, A):
        n = len(A)
        l_arr = [0]*n
        r_arr = [0]*n
        l_arr[0] = A[0]
        r_arr[0] = A[n-1]
        for i in range(1,n):
            l_arr[i] = min(l_arr[i-1], A[i])
        for i in range(n-2, -1,-1):
            r_arr[i] = max(r_arr[i+1], A[i])
        i = j = diff = 0
        while i < n  and j < n:
            if l_arr[i] <= r_arr[j]:
                diff = max(diff, j-i)
                j+=1
            else:
                i+=1
        return diff

A = [3,2,1,4,5,6]
s = Solution()
print(s.maximumGap(A))
