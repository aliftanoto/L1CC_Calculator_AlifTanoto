import math 
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiple(x,y):
    return x * y
def divide(x,y):
    return x / y
def power(x,y):
    return x**y
def square(x,y):
    return math.sqrt(x)
print('select operation')
print('1.add')
print('2.subtract')
print('3.multiple')
print('4.divide')
print('5.power')
print('6.square roots')
choose=input('choose (1,2,3,4,5,6) : ')

num1=float(input('enter the first number : '))
num2=float(input('enter the second number :'))


if(choose=='1'):
    print(num1,'+',num2,'=', add(num1,num2))
elif(choose=='2'):
    print(num1,'-',num2,'=',subtract(num1,num2))
elif(choose=='3'):
    print(num1,'*',num2,'=',multiple(num1,num2))
elif(choose=='4'):
    print(num1,'/',num2,'=',divide(num1,num2))
elif(choose=='5'):
    print(num1,'**',num2,'=',power(num1,num2))
elif(choose=='6'):
    print(num1,'sqr',num2,'=',square(num1,num2))
else:
    print('ERROR')

    
