my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

my_new_list_asc = sorted(my_list)
# my_list.sort() # this function will update my_list
print(my_new_list_asc)
my_new_list_desc = sorted(my_list, reverse=True)
print(my_new_list_desc)
my_sliced_list_even = my_new_list_asc[1::2]
print(my_sliced_list_even)
my_sliced_list_odd = my_new_list_asc[::2]
print(my_sliced_list_odd)

multiple_of_3 = []
for number in my_list:
    if number % 3 == 0:
        multiple_of_3.append(number)
print(multiple_of_3)
print(my_list)