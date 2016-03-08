x = input('enter any number')
x= int(x)

for y in range(2,x):
    if x%y==0:
        print(x, ' is not prime')
        break
    y=y+1
else:
    print(x, 'is prime')
    
    
