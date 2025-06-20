def saiman_noob():
    print('Hello world! Saiman is noob.')

saiman_noob()


def add_num1(a,b):  #a function that adds 2 numbers
    return a+b

sum=add_num1(3,5)
print("The sum is ",sum)


def add_num2():  #a function that takes 2 input numbers, adds and prints the sum.
    a=int(input("Enter number"))
    b=int(input("ENter 2nd number"))
    print("The sum is ",a+b)
    return a+b

sum2=add_num2()
print(sum2)

def greet(name="Guest"):    #function with default  value as guest
    print(f'hello,{name}!')

greet()
greet("Alice")


#Lambda functions (One line function)

#function name=lambda argument: one expression    Syntax
square=lambda x : x*x
print(square(5))

add=lambda x,y:x+y
print(add(3,4))


# Modules
'''There are built in modules and user-built modules'''

import Module_eg
print(Module_eg.greet("ANJAL"))

import math
print(math.sqrt(25))



#A program to find Factorial of a number using function.

def fact(num):
    f=1
    for i in range(1,num+1):
        f=i*f
    return f

print(fact(5))


# user defined function that returns add subtract multiply divide

import mathcalc

print(mathcalc.add(1,2))
print(mathcalc.sub(5,3))
print(mathcalc.mul(1,4))
print(mathcalc.div(2,0))
print(mathcalc.div(14,2))
print(mathcalc.div(10,5))


#WAP a function to find the largest number in a list [2,10,3,55,7]

num=[2,10,3,55,7]

def largest(numbers):
    largest=numbers[0]
    for i in numbers:
        if i>largest:
            largest=i
    return largest

print(largest([1,2,3,4,5,6,7,8,9]))


