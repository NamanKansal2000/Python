class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        str_ = ""
        for i in A:
            str_+=str(i)
        val = int(str_)
        val+=1
        val = str(val)
        return list(map(int,val))


A = [1,2,3]
s = Solution()
print(s.plusOne(A))
