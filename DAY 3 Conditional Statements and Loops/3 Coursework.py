age=20
if(age > 18):
    print("YOU CAN VOTE")
else:
    print("YOU CANNOT VOTE")


print('Hello World')

score=100
if(score>=90):
    print("Grade A")
elif(score>=70):
    print("Grade B")
elif(score>=50):
    print("Grade C")
else:
    print('Fail')


age=int(input('Enter age'))
if age>=18:
    nation=input("Are you  nepali y/n")
    if nation=="y":
        print("You can vote")
    else:
        print("NO YOU ARE NOT NEPALI")
else:
    print("YOU are not 18 years old.")



for i in range(5):
    print(i)


for i in range(1,6):
    print(i)

for i in range(0,10,2):
    print(i)

fruits=['apple','banana','mango']
print(fruits[2])
for fruit in fruits:
    print(fruit)

for i in range(1,3):    #prints 1 and 2 from list not zero
    print(fruits[i])

for i in range(5,0,-1):
    print(i)

n=5
while n>0:
    print(n)
    n=n-1

n=1
while n<=10:
    print(n)
    n=n+2

for i in range(10,0,-1):
    if i==5:
        break
    print(i)


for i in range(10):
    if i==5:
        continue
    print(i)

for i in range(10):
    pass    #holds for loop for future use


# WAP to input a number and checks even or odd
num=int(input("Enter number"))
if num%2==0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

#Create loop that prints numbers form 1 to 20 but it skips multiple of 3 using continue


for i in range(1,21):
    if i%3==0:
        continue
    print(i)

#WAP that prints first 10 numbers of fibonacci sequence using a loop first 10 numbers

n=0
m=1
for i in range(0,5):
    print(n)
    print(m)
    n=m+n
    m=n+m

#Create a guessing game where the user has 3 chances to guess a number correctly using a while loop

org_num=int(input('Enter the number (TO BE GUESSED) '))
print("\n \n \n \n \n \n \n  ")
print('YOU HAVE THREE CHANCE 💖💖💖 TO GUESS A NUMBER')
if org_num%2==0:
    print(f"The number is Even")
else:
    print(f"The number is Odd")
i=0
c=2

heart="💖"
while i<3:
    print('\n.....................')
    gue_num=int(input('Guess the number❓'))
    print('.....................')
    print('\n')
    if org_num==gue_num:
        print(f"✅Correct, The number is {gue_num}")
        print(f"🥇..WIN..🏆\n")
        break
    else:
        print(f'{heart * c} x{c}')
        print(f"😵 {gue_num} is wrong guess☠️")
        if org_num>gue_num:
            print(f'💡HINT:Guess greater than {gue_num}.')
        else:
            print(f'💡HINT:Guess less than {gue_num}.')
    i=i+1
    c=c-1
    
if gue_num!=org_num:
    print(f"The number was {org_num}")


