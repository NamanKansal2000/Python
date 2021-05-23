class solution:
    def _inX(self, x):
        return 0 <= x <= 2/3

    def _inY(self, x):
        return 2/3 < x <= 1

    def _inX1(self, x):
        return 0 <= x < 1/2

    def _inX2(self, x):
        return 1/2 <= x <= 2/3

    def max3(self, max1, max2, max3, current):
        if current >= max1:
            return current, max2, max3
        elif current >= max1:
            return max1, current, max3
        elif current >= max1:
            return max1, max2, current
        return max1, max2, max3

    def max2(self, max1, max2, current):
        if current >= max1:
            return current, max1
        elif current >= max2:
            return max1, current
        return max1, max2

    def min2(self, min1, min2, current):
        if current <= min1:
            return current, min1
        elif current <= min2:
            return min1, current
        return min1, min2
