class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls = [[1]]
        if numRows == 1:
            return ls

        for i in range(1,numRows):
            val = []
            for j in range(i+1):
                if j == 0 or j == i:
                    val.append(1)
                else:
                    val.append(ls[i-1][j-1]+ls[i-1][j])
            ls.append(val)
        return ls
        
