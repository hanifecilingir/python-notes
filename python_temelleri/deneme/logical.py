x=4
hak = 0
devam = 'e'
result = 5 < x < 10

result = (x>5) and (x<10)
result= (hak>0) and (devam == 'e')

result= (x>0) or (x % 2 == 0)

result=not(x>0)

#x, 5-10 arasında olan bir çift sayı mıdır?
result= (((x>5) or (x<10)) and (x%2==0))

print(result)