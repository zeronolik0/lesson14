def print_list(elements):
    if not elements:
        print("Конец списка")
        return
    print(elements[0])
    print_list(elements[1:])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print_list(my_list)