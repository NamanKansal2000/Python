# Function to demonstrate printing pattern triangle
def triangle(n):
    ls = []
    for i in range(0, n):
        ls.append('*' * (2*i+1))
    # print(l)
    width = len(ls[n-1])
    for i in range(0, n):
        print(ls[i].center(width, ' '), end='\n')

    # inverted triangle


# Driver Code
n = int(input())
triangle(n)
