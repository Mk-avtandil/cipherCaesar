def binary_search(my_list, find, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if find == my_list[mid]:
            return mid
        elif find < my_list[mid]:
            return binary_search(my_list, find, start, mid - 1)
        else:
            return binary_search(my_list, find, mid + 1, end)

my_list = [1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 17, 19, 20, 25, 30, 50]
find = 24
x = binary_search(my_list, find, 0, len(my_list))
if x == False:
    print("Item ", find, "Not Found!")
else:
    print("Item ", find, "Found at index ", x)