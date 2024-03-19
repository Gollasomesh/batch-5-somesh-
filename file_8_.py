'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

# Eg:1
# def profile(name, age, place):
#     txt ="my name is ().i am()years.old. i am from()."
#     print(txt.format(name, age, place))
# profile("ipl", 21, "bpl")

# Eg:3
# def profile(name, age, place):
#     txt ="my name is {}.iam{}years old. iam from{}."
#     print(txt.format(name, age, place))
# profile("upi", 22, "pkd")

# Eg:4
# function with return statement
# ! return
# 1.) A variable declared inside the function can be accessed outside the function
# using return
# 2.) return does not prrint anything
# 3.) we cannot write any code below return statement

#     z = 8
#     f1()
# print(z)  ===> error

# def f1(a, b):
#     c = a*b
#     return c
# f1(6, 8)


# def gracemark(object+4):
#     print(object+4)
# gracemark(obj)
# gracemark(obj1)

# ? problem:1
# def palindrome(n):
#     string = str(n)
#     rev = str(n)[::-1]
#     if string==rev:
#         print(n, "palindrome")
# a = int(input("Enter the value: "))
# palindrome(a)
     
#? Based on the declaration of parameter and args
#? functions are divided into 5 catagories

# Positional args
# keyword args
# default args
# variable length args
# keyword variable length args

# The position of parameter ahve to be same as position os arguments
#
# ! Eg:1
# def profile(name, phone, mark):
# txt = "My name is {}. My phone number is {}. I got {} marks."
# print(txt.format(name, phone, mark))
# profile (9878776767, "sidhu", 97) # unexpected output

#*Keyword args
#! Eg:1
# ? To overcome the disadvantage of position args, we use keyword args
# it is the proccess of initialising the parameter with the args while cal;ling the
# ? Function
# def profile(name, phone, mark):
#     txt = "my name is {}. my phone number is {}. I got {}mark."
#     print(txt.format(name, phone, mark))

# profile(name= "ipl", mark=96, phone=9378485389

# todo---> Expection of keywords args afunction
# def profile(name, phone, mark):
#     txt = "My name is {. My phone number is {}. I got {} marks."
#     print(txt.format(name, phone, mark))
    
# profile(name="sid", 123445567, mark=98) # error -> positional arsg follow keywordargs
# profile(123445567, name="sid", mark=98) # error-> name has multiple values
# profile("sid", mark=98, phone=1234556678)

# default args
# ! Eg:1
# def profile(name, phone, place="kadapa"):
#     txt = "may name is {}. my phone number is {}. I am from{}."
#     print(txt, format(name, phone, place))

# profile("somu", 9090909090)    

# ! Eg:2
# def profile(name, phone, place="pkd"):
#     txt = "may name is {}. my phone number is {}. I am from{}."
#     if place=="pkd":
#        print("your eligible")
#     else:
#         print("not eligible")
#     print(txt, format(name, phone, place))

# profile("somu", 9090909090, "pkd")    

# !Exception
#   def profile(name, place="KADAPA", phone): # error coz default args should not follow
#                                       # positional param
#       if place "Kadapa" or place="KADAPA" or place"kadapa":
#          txt "My name is {}, My phone number is {}, I am from {}."
#          print(txt.format(name, phone, place))
#      else:
#          print("You are not eligible to Signup")
#          file("sid", 8767676767)

# variable length params
# ! Eg:1

# if name = 'somu', 'name2', 'name3'
# def profile("name"):
#     for val in name:
#         print("my name is",val)
# profile'sree', 'name2', 'name3'    

# Eg:1
# to pass more than 1 arg to a parameter means we use variable length args
# convert normal paremeter to variable length param, add to ther prefix of param
#    name = "sid", 'name2', 'name3'
#    def profile(*name):
#        for val in name:
#            print("My name is", val)
#    profile("sid", 'name2', 'name3')

#! Eg:2
# def profile (*name, age):
#     for val in name:
#         print("My name is", val, "may age is", age)
# profile("sid", 'name2', 'name3', 28) #error --> age has no args

# def profile(age, *name):
#     for val in name:
#     print("My name is", val, "may age is", age)
# profile (28, "sid", 'name2', 'name3') |

# keyword variable length args
# ! Eg:1
# def price(price_list):
#     print(price_list)

# print(shirt=1000, iphone=80000)

# n =5
# {1:1, 2:4, 3:9, 4:16, 5:25

# n = int(inout("Enter the number:"))

# def dict1(n):
#     d1 = {}
#     for val in range(1, n+1):
#         d1[val] = val**2
#     print(d1)
# dict(s)

# ! ------> object oriented programming
# paradigms of objects oriented programmming
# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation
'''
# ! class is a blue print of an object
 #l1 = [1,2,3,4,5,6]

# Eg:1
# class c1:
#     name1 = "upi"
#     print(name1)

# Eg:2
# class person:
#     name = "upi"

# c = person()
# the procwss of creation of an object is csllled as instantiation
# print(c.name)

# Eg:3
# create of a method
# when the function is created with  a class is called as method

# class person:
#     def display():
#         print("Hello welcome to class")

# p = person()
# p.display()

# ? Eg:4
#! Method with parameter
# class person:
#       def display(person, name, age):
#           print(name, age)
          
# p = person()
# p.display("som", 21)

# ? Eg:5
# class person1:
#       fname = "som" #atteribute or static variable
#       lname = "s"

#       def full_name(self):
#           print(self.fname)
    
#       def full_name(self):
#           print(self.fname+" "+self.lname)
    
# p = person1()
# p.first_name()
# p.full_name()

# ? Eg:6
# constructors ---> __init__()
class profile:
    def __init__(self): # constructor method
        print("reka")

p = profile() # throught this process
        








































