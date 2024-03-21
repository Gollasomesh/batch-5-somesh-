# ploymorphism in classes
# we can achivepolymorphism in 2 ways
# 1.) method over loading --> it is not possible in python
# 2.) method over riding

# ! method riding
# ploymorphism in classes

# ? Eg:1
#class bank:
#    def ratio(self):
#        print("all banks has ropo rate")

#class SBI(bank):
#    def ratio(self):
#        print("SHI rate is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")

#i = 108()
#i.ratio()

#s = SBI()
#s.rstio()

# ? Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("washington Dc")

#class India(USA):
#    def langauge(self):
#        print("None")

#    def capital(self):
#        print("New delhi")

#I = India()
#I.langauge()
#I.capital()

# ! Eg:3
#polymorphism using objects

#c1, c2, --> c1 = print(c1), print(c2)
# f1, f2

#class c1:
#    def f1(self):
#        print("class 1")
    
#classc2(c1):
#    def f1(self):
#        super().f1()
#        p[rint("class 2")

# obj1 = c2()
# obj1.f1()

# obj1 = c2()
# obj2 = c1()
# def display(a):
#     a.fi() #
# display(obj1)
# display(obj2

# changing the functoionality of builtin functions
a=9
b=6
# print(a+b)
# print(a,__add__(B))#? under method or mafic method

# int()
# print(a.__sub__(b))
# len()

# changing the functionality of builtin functions
# class shooping:
#    def __init__(self, 11):
#        self.items = 11

# def len_(self):
#     length len(self.items) 
#     return length
# S = shooping([1,2,3,4])
# print(len(s))

# ! --------> Abstraction
# The process of hiding the implementation details is absraction

# Eg:1

#from abc import ABC,abstractmethod
#class shapes:
#    def sides(self):
#        print("All shapes have sides except circle")

#class triangle(shapes):
#    def traingle_sides(self):
#        print("3 sides")

#    def name(self):
#        print("Iam traingle")

#    def sides(self):
#        pass

#class square(shapes):
#    def square(self):
#        print("4 sides")

#tr = triangle()
#tr.traingle_sides()
#tr.name()

# Rules to define abstract class1

#1.) Abstract class cannot be instantiated
#2.) from abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method
#5.) all the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes

#! Eg:2
# super()---> used to access the parent class method from child class method
#from abc import ABC,abstractmethod
#class c1(ABC):
#   @abstractmethod
#   def m1(self):
#      print("This is abstract class")
#      
#class c2(c1):
#   def m2(self):
#      super().m1()
#      print("Iam child 1")
#
#   def m1(self):
#      pass
#   
#class2 = c2()
#class2.m2()

# EG:3
#from abc import ABC, abstractmethod
#class password(ABC):
#   @abstractmethod
#   def pwd(self):
#      pswd = "somy25$"
#
#class login(password):
#   def validate(self, name, password):
#      if super().pwd() == password:
#         print("welcome", name, "!!")
#         print("login successfull")
#      else:
#         print("please check your password")

#   def pwd(self):
#      pass

#Login = login()
#name = input("enter the name: ")
#pwd = input("enter the passeord: ")
#Login.validate(name, pwd)

# ! Encapsulation
#---> Eg:1
#class car:
#      __name = "BMW" # Private variable

#c1 = car()
#print(c1.name) # error
#c1.name ("Audi")
#print(cl.name) # error

# ---->Eg:2
# ? accessing private data outside the class
#claas c1:
#   __phone = '7656567687'

#  def display(self):
#     print(self.__phone)
#c = c1()
#c.display()


#? declare private method
#class class1:
#    def __mi(self): # Private method
#        print("Iam private method")

#    def __ init __(self):
#        self. m1()
#ce class1()
#c.m1() # error

# ? nested class
# class class1:
#      class class2:
#          name = "sidhu"

#          def display(self):
#             print(self.name)
#       obj1 class2()

#obj = class1()
#obj.obj1.display()

#Write the code for the below tasks using function
#1.) d1 {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30)

#d1 {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
for val in d1:
    if d1[val] = min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('5'):
        print(val)

# class c1:
#    name = "sid"

# obj = c1()
# print(isintance(obj, c1)
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 's'

#2.) Find then 67, is strong number or not

#3.) 11 [1,2,3,4,5,6]
#n=2 --> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]















































































