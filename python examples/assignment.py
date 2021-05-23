def max_of_2(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

def max_of_3(val1, val2, val3):
    return max_of_2(val1, max_of_2(val2, val3))