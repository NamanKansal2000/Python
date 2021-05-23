def f_list(filename):
    list_to_return = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_to_return.append(int(line))
            line = f.readline()
    return list_to_return


primes = f_list('primenumbers.txt')
happies = f_list('happynumbers.txt')

overlaplist = [elem for elem in primes if elem in happies]
print(overlaplist)
