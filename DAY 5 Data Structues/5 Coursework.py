
#LIST

actress=['angel','saiman',"alina"]
print(actress)

actress.append("Ram")
print(actress)

actress.remove("angel")
print(actress)

actress.pop()   #by default removes last value
print(actress)

actress.pop(0)  #removes 0 position value
print(actress)

actress.append("disha")
actress.append("yutta")
print(actress)

actress.sort()
print("Sort data:",actress)

actress.reverse()
print("Sort data in reverse order:",actress)


#Create a shopping list and allow user to add, remove and view items

print("1.Adding lists")
print("2.Remove list")
print("3.Show list")
print("4.Exit")
num=1
Shoplist=[]
while num!=4:
    num=int(input("Type the number for the above functions"))
    if num==1:
        add=input("Enter the name of list ")
        Shoplist.append(add)
        print(Shoplist)
    elif num==2:
        sub=input("Enter the name of list to remove")
        Shoplist.remove(sub)
        print(Shoplist)
    elif num==3:
        print(Shoplist)
    else:
        num=4



#TUPLES ()

numbers=(10,20)
print(numbers[0])

person=("Alia",30,"Actress")
name,age,work=person

print(name)
print(age)
print(work)

student=("Neha",20,"C")
print(student[0])
print(student[1])


#Dictionaries
# word = meaning    
# key = value

std={"name":"Anjal","age":19,"grade":"A"}

std["age"]=100
student["school"]="Mount Olive"
print(student)

#Create a phonebook application using dictionaries
#where users can add and search contacts.

phbook={'name':"Anita","phone":9880}

phbook['phone']=44444
print(f'{phbook[name]}={phbook[phone]}')

ph_book={}
ph_book["Ram"]=111  #Here Ram is key and 111 is its value
ph_book['Shyam']=93830

name="Ram"
if name in ph_book:
    print(f"{name}'s number is {ph_book[name]}")
else:
    print("NOt in contact")


#Sets: unique collection of items {}
 
numb={1,2,3,4,5,6}
print(numb)

# union, intersection
set1={1,2,3}
set2={3,4,5}

print (set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))

#Wap that removes duplicates from a list using a set

list1=[1,2,3,2,1,4,6,23,2,5,1,2,11,1,0]
setA=set(list1)  #typecast
list2=list(setA)
print(setA)
print(list2)

#Wap that takes a sentence as an input 
# and counts the frequency of each word
# using a dictonary.
#Sita is very pretty and she is very smart
#Sita=1 ,is=2, very=2, pretty=1 and-1, she=1, smart=1

sentence=input("Enter a sentence")
words=sentence.lower().split()  #a list made to lower and split sentence into commas
word_count={}   #a dictionary made to count frequency of each word
for w in words:
    if w in word_count:
        word_count[w]=word_count[w]+1
        print(word_count[w])
    else:
        word_count[w]=1
print(word_count)
for w,counter in word_count.items():
    print(f"{w}:{counter}")

