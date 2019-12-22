'''
Вивести усі слова рядка, що написані в нижньому регістрі (усі букви малі).
'''
new_text = str(input())
for word in new_text:
    if word[:] == word[:].lower():
        print((word))