'''
Дано 2 дійсних числа. Вивести середнє значення усіх цілих чисел, що знаходяться між цими двома дійсними числами.
'''

the_first_float = float(input('enter the first float: '))
the_second_float = float(input('enter the second float: '))
range_1 = int(the_first_float)
range_2 = int(the_second_float)
for number in range(range_1, range_2+1):
    my_list = list(' '.join(number))
    middle = sum(my_list)/len(my_list)
    print(middle)