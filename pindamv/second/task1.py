'''
Дано файловий шлях у вигладі списка папок з файлами. Перший елемент списку - диск C/D. Нова папка позначає новий список.
Файли однієї папки збережені в списку одного рівня. Наприклад, ['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', ]]].
Дано звичний шлях до файлу, який необхідно перевірити: D:/tmp/new/folderX. Якщо такий шлях існує, програма повертає ОК. Якщо ні - ERROR.
'''

import re
def create_new_path(folder):
    new_path = []
    index = 0
    for element in folder:
        folder = str(folder)
        folder.split(',')
        element = element[index]
        index += index
        new_path.append(element)
    return '/'.join(new_path)


def file_search(folder, file_path):
    if create_new_path(folder) in file_path:
        return 'OK'
    else:
        return 'ERROR'

print(file_search(['C:', 'backup.log', 'ideas.txt'], 'C/ideas.txt'))
print(file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', ]]], 'D:/tmp/new/folderX'))