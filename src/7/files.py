import os
print(os.getcwd())
#   os.chdir('/')           смена дериктории
#   print(os.getcwd())
#   print(open('files.py')) открытие файла

file = open('files.py')
# print(file)
numer_line = 0

for line in file:
    print(str(numer_line) + ' ' + line)
    numer_line += 1

file.close()


# with open('files.py') as file_2:
#     for line in file_2:
#         print(line)

