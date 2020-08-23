fruits = ['banana', 'pineapple', 'apple']
print(fruits)
vegetables = ['cucumber', 'tomato', 'potato']
fruits_and_vegetables_plus = fruits + vegetables
print(fruits_and_vegetables_plus)
fruits_and_vegetables_extend = []
fruits_and_vegetables_extend.extend(fruits)
fruits_and_vegetables_extend.extend(vegetables)
print(fruits_and_vegetables_extend)
fruits.append('strawberry')
print(fruits)
fruits.insert(1, 'watermelon')
print(fruits)
print(len(fruits))
print(fruits[1])
print(fruits[-1])
print(fruits[-2])
print(fruits[1:4])
print(fruits[:3])
print(fruits[2:])
print(fruits[2:-1])
print(fruits[2:0])  # not possible


fruits.append('banana')
print(fruits)
print(fruits.count('banana'))
print(fruits.count('pineapple'))
print(fruits.count('undefined'))
print('banana' in fruits)
print('undefined' in fruits)

print(fruits.index('banana'))

del fruits[0]
print(fruits)

fruits.append('banana')
fruits.remove('banana')
print(fruits)

fruits.remove('banana')
print(fruits)

print(fruits.pop())
print(fruits)
print(fruits.pop(1))  # bad practice
print(fruits)

print(list(range(0, 12)))
for i in range(0, 12):
    print(i)
for _ in range(0, len(vegetables)):
    print(vegetables)
    print(vegetables.pop())

fruits_immutable = ('banana', 'pineapple', 'apple')
vegetables_immutable = ('cucumber', 'tomato', 'potato')
fruits_and_vegetables_immutable = fruits_immutable + vegetables_immutable
# изменять кортежи нельзя, можно применять другие любые операции которые их не изменяют
print(fruits_and_vegetables_immutable)

(x, y, z) = fruits_immutable
print(x)
print(y)
print(z)

fruits_set = {'banana', 'apple', 'banana'}
print(fruits_set)
fruits_set.add('pineapple')
fruits_set.add('apple')
print(fruits_set)

fruits.append('banana')
fruits.append('banana')
print(fruits)
print(set(fruits))

nested = [
    [
        [1, 2, 3],
    ],
    [
        [1, 2, 3],
    ],
    [
        [1, 2, 3],
    ],
]
print(nested[1][0][1])