old_list = [10,75,43,15,-4,27]
new_list = old_list.copy()

def bubble_sort(my_list):
    last_item = len(my_list) - 1
    for i in range(0, last_item):
        for j in range(0, last_item - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

bubble_sort(new_list)

print("old_list ", old_list)
print("new_list ", new_list)