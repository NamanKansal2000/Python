def anagram(arr, n):
    dict = {}
    for i in range(n):
        word = ''.join(sorted(arr[i]))
        if word not in dict:
            dict[word] = [i+1]
        else:
            dict[word].append(i+1)
    print(dict)

arr = ['dog', 'cat', 'act' , 'tca']
anagram(arr, len(arr))
