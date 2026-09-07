numbers = {1,3,5,2,6,7,9,8,4,10}
print(numbers)
numbers.add(11)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.update((14,9))
print(numbers)
for i in numbers :
    print(i)

number1 = {1,4,2,3}
number2 = {6,3,4,5}
print(number1)
print(number2)
print(number1.union(number2))
print(number1.intersection(number2))
print(number1.difference(number2))
print(number2.difference(number1))
print(number1.symmetric_difference(number2))
number3 = {3,4}
print(number1.issuperset(number3))
print(number1.issubset(number3))
print(number2.issuperset(number3))
print(number2.issubset(number3))
print(number3.issubset(number1))
print(number3.issuperset(number2))