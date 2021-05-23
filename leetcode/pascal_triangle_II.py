class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        c = 2
        ls = [0]*(rowIndex+1)
        ls[0] = 1
        ls[1] = 1
        val = ls[:c]
        while c <= rowIndex:
            ls[c] = 1
            for i in range(1,c):
                ls[i] = val[i-1]+val[i]
            val = ls[:c+1]
            c+=1
        return val



        
