s1 = input("Введіть шлях до файла: ")
folders = s1.split('\\')
print("Шлях до файла:")
for folder in folders[:-1]:
    print(folder)
filename = folders[-1]
dot_index = filename.rfind('.')
if dot_index == -1:
    name = filename
    extension = ''
else:
    name = filename[:dot_index]
    extension = filename[dot_index+1:]
print(f'Назва файла: {name}, Розширення: {extension}')
