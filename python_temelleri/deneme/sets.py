fruits={'orange','apple','banana'}
#print(fruits)[0]  indekslenemez.

for x in fruits:
    print(x)

fruits.add('cherry')
print(fruits)
fruits.update(['mango','grape'])
fruits.remove('mango')
fruits.discard('apple')
fruits.pop()
print(fruits)

fruits.clear()
print(fruits)
# myList=[1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))