numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

val=min(numbers)
val=max(numbers)
val=max(letters)
val=min(letters)
val=numbers[3:6]
val=numbers[:3]
val=numbers[4:]

numbers[4]=40
numbers.append(49)
#numbers.insert(3,78)
numbers.insert(-1,52)
# numbers.pop()
# numbers.remove(9)
# numbers.sort()
letters.sort()
# numbers.reverse()
letters.reverse()
print(numbers.count(10))
print(letters.count('b'))

numbers.clear()
print(numbers)




# print(numbers)
print(letters)

