def postfix(arr,n):
    operator = ['+', '-', '*', '/', '%']
    stack = []
    for i in arr:
        if i not in operator:
            stack.append(i)
        else:
            first = int(stack.pop())
            second = int(stack.pop())
            if i == '+':
                stack.append(first + second)
            elif i == '-':
                stack.append(first - second)
            elif i == '/':
                stack.append(first / second)
            elif i == '*':
                stack.append(first * second)
            elif i == '%':
                stack.append(first % second)
    print(stack[-1])

arr = ['2', '1', '+', '3', '*']
postfix(arr, len(arr))
