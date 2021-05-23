class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        if len(a) < len(b):
            a,b = b,a
        a = a[::-1]
        b = b[::-1]
        c = ''
        for i in range(len(b)):
            s = int(a[i]) + int(b[i]) + carry
            if s == 0:
                c+='0'
                carry=0
            if s == 1:
                c+='1'
                carry = 0
            if s == 2:
                c+='0'
                carry = 1
            if s == 3:
                c+='1'
                carry = 1
        if carry == 0:
            c+=a[len(b):]
            return c[::-1]
        for i in range(len(b),len(a)):
            s = int(a[i])+carry
            if s == 0:
                c+='0'
                c+=a[i+1:]
                return c[::-1]
            if s == 1:
                c+='1'
                c+=a[i+1:]
                return c[::-1]
            if s == 2:
                c+='0'
                carry = 1
            if s == 3:
                c+='1'
                carry = 1
        if carry:
            c+='1'
        return c[::-1]
            
