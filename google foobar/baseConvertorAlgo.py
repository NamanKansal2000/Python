from pythonds.basic import Stack


def baseConverter(num, base):
    digits = '0123456789ABCDEF'
    remStack = Stack()
    while num > 0:
        rem = num % base
        remStack.push(rem)
        num = num//base
    new_str = ''
    while not remStack.isEmpty():
        new_str += digits[remStack.pop()]

    return new_str


print(baseConverter(26, 26))
print(baseConverter(256, 16))
print(baseConverter(25, 8))
