# List comprehension
# This code finds even from a given list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_a = [a[i] for i in range(len(a)) if a[i] % 2 == 0]
print(even_a)
