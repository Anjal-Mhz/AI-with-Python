# Create a Python script to count how many times a particular word appears in a file.
# Extract all email addresses from a file using regex.

with open('sample2.txt','r') as file:
    content=file.read()

import re

word=input("Enter a word that u want to count in sampele2.txt file  :")

pattern1=rf'\b{word}\b'
match1=re.findall(pattern1, content, re.IGNORECASE)
print(match1)
print(f'{word}={len(match1)}\n')



pattern2=r'\b[a-zA-Z0-9_+]+@[A-Za-z0-9.]+\b'
match2=re.findall(pattern2,content)
match3=set(match2)
print(f"The emails are\n {match3}\n")