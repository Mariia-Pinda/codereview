'''
Знайти суму усіх дійсних чисел, що знаходяться в списку.
'''

new_list = list(input())
for elements in new_list:
    if isinstance(elements, float):
        my = elements
        print = (sum(elements))
