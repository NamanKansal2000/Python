def common_letters():
    str1 = set(input("Enter first str: ").lower())
    str2 = set(input("Enter second str: ").lower())
    print(str1&str2)
common_letters()
