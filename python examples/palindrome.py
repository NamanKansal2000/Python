def is_palindrome(input_string):
    ls = input_string.split()
    str = ''.join(ls)
    new_string = str.lower()
    reverse_string = new_string[::-1]
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome('Never Odd or Even'))
