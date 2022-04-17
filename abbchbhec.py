person={
    'fname':'VRAJ','lname':'PATEL',
    'address':{'Street Name':'ABCDEFGH','Street No':'1234','pincode':'883444'},
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    }
#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
skills='skills'
if skills in person.keys():
    if len(person.get(skills))%2==1:
        print(person.get(skills)[len(person.get(skills))//2])
    else:
        print(person.get(skills)[len(person.get(skills))]/2)
#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
skills='skills'
if skills in person.keys():
    if 'Python' in person.get(skills):
        print('Person Has Python Skill ...')
    else:
        print('Person Does Not Have Python Skill ...')
"""
If a person skills has only JavaScript and React, print('He is a front end developer'),
if the person skills has Node, Python, MongoDB,print('He is a backend developer'), 
if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
else print('unknown title') - for more accurate results more conditions can be nested!
"""
skills='skills'
if skills in person.keys():
    if ['JavaScript','React'] == person.get(skills):
        print('He is a front end developer ...'.title())
    if 'Node' and 'Python' and 'MongoDB' in person.get(skills):
        print('He is a backend developer ...'.title())
    if 'React' and 'Node' and 'MongoDB' in person.get(skills):
        print('He is a fullstack developer ...'.title())
    else:
        print('unknown title'.title())
#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even=0
odd=0
for i in range(100):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print('sum of all even numbers is :'.title(),even,'\nsum of all odd numbers is :'.title(),odd)
#Write a functions which checks if all items are unique in the list.
def UniqueChecker(list):
    for i in list: