# lst = input("Enter a list of elements")
print("Use binary search to find the element")


def find(lst, element_to_find):
    lst.sort()
    start_index = 1
    end_index = len(lst) - 1

    while True:
        mid_index = (end_index - start_index)//2
        mid_value = lst[mid_index]
        if mid_index < 0 or mid_index > end_index or mid_index < start_index:
            return False

        elif mid_value == element_to_find:
            return True
        elif mid_value > element_to_find:
            start_index = mid_index
        elif mid_value < element_to_find:
            end_index = mid_index
        else:
            return False


def loop(lst, element_to_find):
    lst.sort()
    for element in lst:
        if element == element_to_find:
            return True
    return False


lst = [1, 3, 5, 30, 42, 43, 500, 50]
# result = loop(lst, 500)
result = find(lst, 5)
print(result)
