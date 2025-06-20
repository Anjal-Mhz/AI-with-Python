'''
 write a program to:
1. take input from user of two numbers.
2. perform arithmetic operation
3. checks if the first number is greater than the second number using comparison operator
4. print the results.
'''

num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))

sum=num1 + num2
difference=num1-num2
multiply=num1*num2
divide=num1/num2
modu=num1%num2

print('\n..........................................')


print(f'The sum of {num1} and {num2} is {sum}')
print(f'The difference of {num1} and {num2} is {difference}')
print(f'The multiply of {num1} and {num2} is {multiply}')
print(f'The division of {num1} and {num2} is {divide}')
print(f'The modulus of {num1} and {num2} is {modu}')

print('\n..........................................')


if num1>=num2:
    print(f'{num1} is greater or equals to {num2}.')
else:
    print(f'{num1} is not greater or equals to {num2}.')