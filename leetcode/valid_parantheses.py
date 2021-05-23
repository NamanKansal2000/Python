class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        d = {'[':']', '(':')', '{':'}'}
        for i in s:
            if i in d.keys():
                ls.append(i)
            else:
                if len(ls) == 0:
                    return False
                val = ls.pop()
                if d[val] != i:
                    return False
        if len(ls) >0 :
            return False
        return True
        
