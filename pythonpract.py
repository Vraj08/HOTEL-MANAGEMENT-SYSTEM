
###         DICTIONARY           ###

# Write a Python script to check whether a given key already exists in a dictionary.
print('Q1) Write a Python script to check whether a given key already exists in a dictionary.'.title())
print()
print('now implementing the following Question'.title())
print()
def KeyPresentOrNot(dict, key):#This is a function which checks if the given key is present in the dictionary or not it takes the key and dictionary as arguments
    if key in dict.keys():#This line will check if the given key is present in the dictionary if it is present it will return true
        print('the given key'.title(),key,"already exists in the given dictionary".title())
        print()
    else:
        print('the given key'.title(),key,"does not exist in the given dictionary".title())
        print()
dict = {'V': 88, 'R': 888, 'A': 8888,'J':88888}
print('the given dictionary is '.title(),dict)
print()
key = 'V'
print('now checking if the key '.title(),key,'already exists in the above dictionary or not'.title())
print()
KeyPresentOrNot(dict, key)#Calling the function created above
key = 'I'
print('now checking if the key '.title(),key,'already exists in the above dictionary or not'.title())
print()
KeyPresentOrNot(dict, key)#Calling the function created above
print()
print()

# Write a Python script to merge two Python dictionaries.
print('Q2) Write a Python script to merge two Python dictionaries.'.title())
print()
print('now implementing the following Question'.title())
print()
dict1 = {'V': 88, 'R': 888,'A':8888,'J':88888}
dict2 = {'P': 4, 'A': 44,'T':444,'E':4444,'L':44444}
dict3={}
print('The First Dictionary is : '.title(),dict1)
print('The Second Dictionary is : '.title(),dict2)
dict3.update(dict1)#this will add dict1 to empty dict3
dict3.update(dict2)#this will add dict2 to dict3
print('The Dictionary After Merging Both First and Second dictionaries is : '.title(),dict3)
print()
print()

#Write a Python program to sum all the items in a dictionary.
print('Q3) Write a Python program to sum all the items in a dictionary.'.title())
print()
print('now implementing the following Question'.title())
print()
dict = {'V': 88, 'R': 888, 'A': 8888,'J':88888}
print('The given dictionary of which we are going to find sum is : '.title(),dict)
print()
values = dict.values()#This command will extract all the values from the dictionary
print("Sum of all items in the above dictionary is :", sum(values))#This line will sum all the values and print them
print()
print()

#Write a Python script to add a key to a dictionary.
print('Q4) Write a Python script to add a key to a dictionary.'.title())
print()
print('now implementing the following Question'.title())
print()
dict = {'V':88, 'R':888,'A':8888}
print('this is the dictionary in which we are going to add a new key'.title(),dict)
print()
dict.update({'J':88888})#This will add/merge this dictionary given in the argumment to the dict
print('the dictionary after adding new key is : '.title(),dict)
print()
print()

#Write a Python script to concatenate following dictionaries to create a new one.
print('Q5) Write a Python script to concatenate following dictionaries to create a new one.'.title())
print()
print('now implementing the following Question'.title())
print()
dic1={'V':8, 'R':88}
print('The dictionary 1 is : '.title(),dic1)
dic2={'A':888, 'J':8888}
print('the dictionary 2 is : '.title(),dic2)
dic3={'I':88888,'H':888888}
print('the dictionary 3 is : '.title(),dic3)
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)#this will add all the elements from all the dictionaries to empty dictionary dict4
print('the dictionary 4 after concatenating all the above three dictionaries is : '.title(),dic4)
print()
print()

###         TUPLE           ###

#Write a Python program to create a tuple with different data types.
print('Q1) Write a Python program to create a tuple with different data types.'.title())
print()
print('now implementing the following Question'.title())
print()
tup = ("String", False, 3.2, 1)#This is a tuple contaning string,boolean,float,int datatypes
print('Printing tuple with different datatypes : '.title(),tup)
print()
print()

#Write a Python program to create a tuple with numbers and print one item.
print('Q2) Write a Python program to create a tuple with numbers and print one item.'.title())
print()
print('now implementing the following Question'.title())
print()
tup = 5, 10, 15, 20, 25#This contains a tuple with numbers
print('This is a tuple contaning numbers : '.title(),tup)
tup = 5,#This will overwrite tuple and store one number
print('now printing one item : '.title(),tup)
print()
print()

#Write a Python program to add an item in a tuple.
print('Q3) Write a Python program to add an item in a tuple.'.title())
print()
print('now implementing the following Question'.title())
print()
tup1 = ("Vraj", "Patel")
print('this is the original tuple in which we are going to add one element : '.title(),tup1)
print()
tup2 = ("V...",)
tup1 = tup1 + tup2#this will add tuple1 and tuple2
print('the tuple after adding new element is : '.title(),tup1)
print()
print()

#Write a Python program to convert a tuple to a string.
print('Q4) Write a Python program to convert a tuple to a string.'.title())
print()
print('now implementing the following Question'.title())
print()
def ConvertTupleToString(tup):#this is a function which will convert tuple into string it will take tuple as argument
    str = ''#this is a null string
    for item in tup:
        str = str + item#we are ititrating tuple one by one and then adding it to the null string declared at beginning
    return str
tuple = ('V', 'R', 'A', 'J')
print('this is the tuple that we are going to convert into string : '.title(),tuple)
print()
str = ConvertTupleToString(tuple)
print('After converting the tuple into string the string is : '.title(),str)
print()
print()

#Write a Python program to find the length of a tuple.
print('Q5) Write a Python program to find the length of a tuple.'.title())
print()
print('now implementing the following Question'.title())
print()
tup = ('V','R','A','J')
print('this is the tuple of which we are going to find the length : '.title(),tup)
print()
print('the length of the tuple is : '.title(),len(tup))#len function will find the length of tuple
print()
print()

###         SET           ###

#Write a Python program to add member(s) in a set and clear a set.
print('Q1) Write a Python program to add member(s) in a set and clear a set.'.title())
print()
print('now implementing the following Question'.title())
print()
set = {'VRAJ'}
print('this is the original set in which we are going to add elements : '.title(),set)
set.add("Patel")#This will add only a single element to set
print("\nNow after adding a single element 'Patel' the set now is : ".title(),set,'\n')
set.update(["V...", "P..."])#this will add the elements of list as element in the set
print("Now after adding a multiple elements 'V...','P...' the set now is : ".title(),set,'\n')
set.clear()#this will clear the set
print("Now after clearing the set now the set is : ".title(),set,'\n')
print()
print()

#Write a Python program to remove an item from a set if it is present in the set.
print('Q2) Write a Python program to remove an item from a set if it is present in the set.'.title())
print()
print('now implementing the following Question'.title())
print()
set = {'VRAJ','PATEL','V...','P...'}
print('This is the original set in which we are going to remove a element if it is present in the set : '.title(),set,'\n')
print("Now we will remove 'R...' if present in the set ...".title())
set.discard('R...')#this function will remove the element passed in the argument if present in set
print("the set after removing 'R...' if present in the set is : ".title(),set,'\n')
print("Now we will remove 'V...' if present in the set ...".title())
set.discard('V...')
print("the set after removing 'V...' if present in the set is : ".title(),set,'\n\n')

#Write a Python program to create an intersection, Union, difference of sets.
print('Q3) Write a Python program to create an intersection, Union, difference of sets.'.title())
print()
print('now implementing the following Question'.title())
print()
A = {8, 88, 888, 8888, 88888}
B = {8, 88, 444, 4444, 44444}
print('This is the set a '.title(),A,'\nThis is the set b '.title(),B,'\n')
print("Union of A and B is :".title(), A | B)# this operator | will given union of two sets
print("Intersection of A and B is :".title(), A & B)# this operator & will given union of two sets
print("Difference of A and B is :".title(), A - B,'\n\n')# this operator - will given union of two sets

#Write a Python program to find maximum and the minimum value in a set.
print('Q4) Write a Python program to find maximum and the minimum value in a set.'.title())
print()
print('now implementing the following Question'.title())
print()
set = {8888, 888, 8, 88, 888888, 88888}
print("Original set in which we are going to find min and max elements is : ".title(),set,'\n')
print("Maximum element in set is :".title(),max(set),'\n')#max function will give the max value present in set
print("Minimum element in set is :".title(),min(set),'\n\n')#min function will give the min value present in set

#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#most common from list
def commonelementfinder(list):#this is a function which will take list/tuple as argument and then it will convert them to set and return  the most common element in them
    return max(set(list), key = list.count)#i have used this function to find common element and count function to count the frequency of the common element
print('Q5) Write a Python program to find the most common elements and their counts from list, tuple, dictionary.'.title())
print()
print('now implementing the following Question'.title())
print()
LIST = [8, 4, 8, 4, 44, 88,8,8,888,444,444,8888,8,4,8,8,4]
a=commonelementfinder(LIST)
print('This is the list from which we are going to find most common element and its count : '.title(),LIST,'\nThe most common element from the above list is : '.title(),a,'and it occurs '.title(),LIST.count(a),'times in the list'.title(),'\n')
#most common from tuple
TUP = (888, 4, 88, 4, 4,4,4,8,888,444,444,8888,8,4,4,8,4)
a=commonelementfinder(TUP)
print('This is the tuple from which we are going to find most common element and its count : '.title(),TUP,'\nThe most common element from the above tuple is : '.title(),a,'and it occurs '.title(),TUP.count(a),'times in the Tuple'.title(),'\n')
#most common from dictionary
DICT={1:88,2:22,3:33,4:88,5:88,6:44,7:34,8:88}
LiST=list(DICT.values())
a=commonelementfinder(LiST)
print('This is the Dictionary from which we are going to find most common element and its count : '.title(),DICT,'\nThe most common element from the above dictionary is : '.title(),a,'and it occurs '.title(),LiST.count(a),'times in the Dictonary'.title(),'\n\n')
