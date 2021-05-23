def is_palindrome(str):
    str = str.strip()
    words = str.split(' ')

    for word in words:
        word = word.lower()
        str = ''.join(word)
        # print(str)
    reverse = str[::-1]
    if str == reverse:
        return True
    else:
        return False


str = input('Enter a string to check palindrome: ')
result = is_palindrome(str)
if result:
    print(str + ' is palindrome')
else:
    print(str + ' is not palindrome')
