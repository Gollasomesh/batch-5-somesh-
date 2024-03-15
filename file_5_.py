# ! ------> common functions for list

# l1 = [6, 7, 8, 9, 0]
# print(len(11))

# print(max(11))
# print(min(11))

# l1=[6, 8, 9, "p", "u"]
# print(max(11)) # --> error coz its a combination of lnt and string
# print(min(11)) # --> error coz its a combination of int and string

# l1 =[6, 7, 8, 9, 0,ArithmeticError 8.89, -5, 0.78]
# print(min(11)) # -5

# l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value of specific element
# print(l1.count(6))

#! some functions which is specificallyused for list

# To add element inside list
# insert() --> to add element at specific inde position
# l1 = [6,6,6, 7, 8, 9, 0, 8,89, -5, 0.78]
# l1.insert(2, "cars")
# print(11)

# ? To delete element from list
# 11 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
# pop() ---> last element will be deleted
# 11. pop(4) # 4 is index value
# print(11)

# remove(element) --> used to delete element directly
# l1.remove(8.89)
# print(11)

# clear()--> to complete delete all element in list
# l1.clear()
# print(11)

# del -> to delete the list
# del 11 #or del(l1)
# print(l1)

# ? ----> join 2 lists

# l1 = [9, 0, 8]
# l2 = ["p", "o", "t", 34]
# print(l1+l2)

# ! or

# extend() --> to combine 2 lists
# l1.extend(l2)
# print(l1)

# ? -------> copy()
# l1 = [6, 7, 8, 9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))

# ! diff between shallow copy and deep copy

# shallow copy
# import copy
# l1 = [8, 9, 0,[5,6], [3, 2, 1]]
# l2 = copy.copy(l1)
# l1.append(890)
# print(l1)
# print(l2)


# deep copy
# import copy
# l1 = [8, 9, 0,[5,6],[3, 2, 1]]
# print(l1[-1][1]) --> to index nested list

# 12 = copy.copy(l1)
# l1[-1].append('cars')
# print(l1)
# print(l2)

# ? sort --> arrange elements in list inascending or decending order
# l1 = [9, 7, 45, 0,-6, 5, 12]
# l1.sort() # to arrange in ascending order
# print(l1)

# l1.sort(reerse=true) # to sort in descending order
# print(l1)

# l1 = ['z', 'i', 'o', 'p', 9]
# l1.sort()
# print(l1) # --> error

# ? list constuctor
# list() --> to conver other collection datatype to list
# 13 = ((8, 9, 0))
# print(list(13))

# 14 = (8, 9)
# print(list(14))

# ! ---> nested list

# l1 = [8, 9, [0, 8, 7], ["p", "o", 'y'], [8, 't']]
# print(l1[-2][1]) # --> o

# print(l1[1:4])
# print(l1[1:-1])

# ? to delete "t"from l1
# l1[-1].remove("t")
# prnt(l1)

# ? combine these ["o", "o",'y'], [8,'t']lists in l1 to ["p", 'o','y', 8, 't']

# l1 = ['p', 'o', 'y']
# l2 = [8, 't']
# l1.extend(l2)
# print(l1)

#  ---> Tuple
# char of tuple

# 1. tuple have to be surrounded by ()
# 2. The elements inside tuple are not changable
# 3. The elements inside tuple are indexed
# 4. The element will execte in order
# 5. It is heterogenous
# 6. It allow duplicate elements

# Eg:1
# t1 =ss list (8,8,9,6,5.78,[9,0],(6,8),"upi",9+6j)
# print(t1)
# print(type(t1))  ==> class tuple

# indexing, slicing are all same as list

# l1 = [8]
# print(type(l1))  ==> class list


# l1 = (8)
# print(type(l1)) ==> int


# l1 = (8,)
# print(type(l1)) ==> tuple

# t1 = 8,9
# print(type(t1) ==> tuple

# t2 = 8,
# print(type(t2))  ==> tuple

# len(), min(),max(), index(), count() --> all same as list

# to add elements inside tuple --> cannot add

# t1 = (8,9,0)
# t2 = (6,7,8)
# print(t1+t2) --> (8, 9, 0, 6, 7, 8)

# t1 =(8, 9, 0,89,12)
# print(tuple(sorted(t1)))
# print(tuple(sorted(t1, reverse=true)))

# l1 = [9, 8, 0, 6, 5]
# for i in l1:
#     print(i)

# ! ----> strings
# s1 = "0"
# print(type(s1))

# s1 = "u"
# print(type(s1))

# s1 = "hello world"
# To access string
# print(s1)
# indexing and slicing ---> same as list and tuple
# print(s1[0:5])

# len(), min(), max(), index(), count()
# s1 = "hello world"
# print(len(s1))
# print(max(s1))
# print(min(s1))
# ord() --> used to find the ASCIT Value of a character
# s1 = 'u'
# print(ord(s1))

# function of string
# s1 = "hello world"

# ? to convert all characters to upper case
# print(s1.upper())

# ? to conver to lower case
# s1 = "HFREDGiou"
# print(s1.lower())

# strip() --> to eliminate the space in beginning and end of string
# s1 = " where are you?"
# print(s1.lstrip())

# print(ls.lstrip())
# print(1s.rstrip())
# print(1s.sstrip())

# split() --> to split the wordsin string based on a charecter
# s1 = "where are you?"
# print(s1.split())
# print(s1.split("r"))

# replace()
# s1 = "where are you?"
# print(s1.replace('r', '&&'))  ==> whe&&e a&&e you?

# swapcase() --> to convert capital to small to capital at a time
# s1 = "HEY there"
# print(s1.swapcase()) ==> hey THERE

# title() --> to write the string in format of title
# s1 = 'never giveup'
# print(s1.title())

# capitalize()--> 1st char of string will be converted to capital
# s1 = "hello"
# s2 = 'world'
# print(s1+s2)

# s1 = '''
# how are you
# iam fine
# hey there
# '''
# splilines() --> used to split the string based on lines
# print(s1.splitlines())

# find () --> to find the index based on a charecter
# s1 = "hello world"
# print(s1.find('h'))
# print(s1.index('h'))

# join() -->
# l1 = ["hey', "there"]
# print(" ",join(l1))
# print("$",join(l1))      

# s1 = "welcome to all"
# print(s1.endswith('l'))
# print(s1.startswith('w'))

# s1 = "67"
# print(type(S1))
# print(s1.isdigit())

# print the string in reverse manner
# s1 = "welcome to all"
# print(s1[::-1])

# ! -----> eg:1
# wap to find the number of lower case letters
# s1 = "HEY there you ARE"
# count = 0
#  for i in s1:
#      if i.islower():
#          count+=1
# print('the total num of lower case letters:",count)


# ! -----> Eg:2 r----> "$"
# s1 = 'restarter'
# s1 = "IMAGIN"
# fst = s1[0]
# bal = s1[1:]
# txt = bal.replace(fst, "$")
#

# s1 = "Lorem Ipsum is simply dummy textof the printing and typesetting industry.Lorem Ipsum has been the industry's standarddummy text ever since the 1500s, when anunknown printer took a galley of type andscrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
# charecter = len(s1)
# print(charecter)

# words = s1.split(" ")
# print(len(words))

sentenses = s1.split(',')
for val in sentenses:
    if val =='':
        index = sentenses.index(' ')
        sentenses.pop(index)
print(len(sentenses))





































 





















