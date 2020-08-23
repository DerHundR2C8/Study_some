is_valid = True
if is_valid:
    print('valid')
else:
    print('Not valid')

is_number = True
is_valid = False
if is_valid:
    print('valid')
elif is_number:
    print('not valid but number')

if is_valid or is_number:
    print('valid or number')

is_valid = True

if is_valid and is_number:
    print('valid number')

num1 = 10
num2 = 20000
num3 = 0
num4 = -1256


if num1:
    print('num1 is true')
if num2:
    print('num2 is true')
if num3:
    print('never see this masseg')
if num4:
    print('Num4 it is true(works)')

if num1 < num2:
    print('Num1 is less than num2')
if num2 > num3:
    print('Num2 is greater than num3')
if num1 == 10:
    print('Num1 is equal 10')

str1 = ''
str2 = 'word'
str3 = ' '

if str1:
    print('it never happens')
if str2:
    print('it True')
if str3:
    print('it True')


list1 = []
list2 = ['12', 122]

if list1:
    print('list1 is not True')
if list2:
    print('list2 is it True')


dict1 = {'key1': 'not_key1'}
dict2 = {}
dict3 = {False: False}

if dict1:
    print('Dict1 it is true')
if dict2:
    print('Dict2 it is False')
if dict3:
    print('dict3 it is True')

nothing = None
if nothing:
    # IT IS WRONG
    print('It is False')

if nothing is not None:
    print('unreachable')

if nothing is None:
    print('possible')