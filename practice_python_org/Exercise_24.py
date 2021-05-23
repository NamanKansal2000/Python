def verticle(size):
    print('|    '*(size + 1))


def horizontal(size):
    print(' --- '*size)


size = int(input('Enter the size of board: '))

for i in range(size):
    horizontal(size)
    # print()
    verticle(size)
    # print()

horizontal(size)
