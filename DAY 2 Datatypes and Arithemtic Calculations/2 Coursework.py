name="anjal"
school="merocodingclass"
city=10
is_female=True
marks=100
marks=65 #prints this value of marks
age=10
num=7

print("Hello python")

print('\n..........................................')

print(name)
print(school)
print(city)
print(is_female)
print(marks)

print('\n..........................................')

print(f"my name is {name}. I study in {school}")
print("Hello, My first name is",name,"I am studying in ",school)
print(f"my age is {age}")
print(f"in five years, my age is {age+5}")
print(f"is number greater than 5?{num >5}")

print('\n..........................................')

age="25"
int_age=int(age)

print(type(int_age))
print(type(age))

print(int_age + 5)
print('\n..........................................')

age=35
str_age=str(age)
print(type(str_age))
print(type(age))

print('\n..........................................')

#Operators

first_value=10
second_value=20

total=first_value + second_value
print(total)

print('\n..........................................')

#A program to create basic arithmetic calculation

a=10
b=20

#Arithmetic Operator
sum=a + b
diff=a-b
mult=a*b
div=a/b
modu=a%b

print(sum,diff,mult,div,modu)

#Logical Operator
print(a>5 and a<20 and a==11)
print(a>5 or a<20 or a==11)

#Comparison Operator

print(a>b,a<b,a==b,a!=b)

print('\n..........................................')


#Write a progeram to maek a simple claculator in python

a=int(input("What is your first number?"))
b=int(input("What is your second number?"))

sum=a + b
diff=a-b
mult=a*b
div=a/b
modu=a%b

print("Choose the function")
print("1.Sum")
print("2.Difference")
print("3.Multiply")
print("4.Division")
print("5.Modolus")

num=int(input("Choose the no for function"))

if num==1:
    print(sum)
elif num==2:
    print(diff)
elif num==3:
    print(mult)
elif num==2:
    print(div)
else:
    print(modu)



