class Solution:
    def spiralOrder(self, a):
        row = col = 0
        top, bottom = 0, len(a)-1
        left, right = 0, len(a[0])-1
        b = []
        if len(a) == 1 :
            return a[0]
        if len(a[0]) == 1:
            for i in range(len(a)):
                b.append(a[i][0])
            return b
        while top <= bottom and left <= right:
            for col in range(left, right+1):
                b.append(a[row][col])
            top+=1
            if top <= bottom:
                for row in range(top, bottom+1):
                    b.append(a[row][col])
                right-=1
            else:
                break
            if left <= right:
                for col in range(right, left-1, -1):
                    b.append(a[row][col])
                bottom-=1
            else:
                break
            if top <= bottom:
                for row in range(bottom, top-1, -1):
                    b.append(a[row][col])
                left+=1
            else:
                break
        return b

A = [
  [133, 241, 22, 258, 187, 150, 79, 207, 196, 401, 366, 335, 198],
  [401, 55, 260, 363, 14, 318, 178, 296, 333, 296, 45, 37, 10],
  [112, 374, 79, 12, 97, 39, 310, 223, 139, 91, 171, 95, 126]
]
s = Solution()
print(s.spiralOrder(A))
