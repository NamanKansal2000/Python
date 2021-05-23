def reverse_word_order(str):
    str = str.strip()
    words = str.split(' ')
    words.reverse()
    new_str = ' '.join(words)

    return new_str


print('This code will print the reversed word order')
# reversed_string = reverse_word_order('My name is Michele')
reversed_string = reverse_word_order(input("Enter the string: "))
print(reversed_string)
