# 2.) find the uncommon words from 2 strings
# s1 = "hello how are you"
# s1 = "hello how is"

# s1 = "hello how are you"
# s2 = "hello how is"

# for val in s1:
#     if val not in s2:
#         print(val)

# for val in s2:
#     if val not in s1:
#         print(val)


# ? Eg:2
# unparametarised constructor
# class profile:
#     def __init_(self):
#       print("hello world")

# obj profile()
# obj._init__()

#? Eg: 3
# Parametarised Constructor
# class profile:
#     def __init__(self, id, name, age):
#        print(id, name, age)

# obj = profile(1, "roy", 29) 

#? Eg:4
# class c1:
#     name = "sid"
#     place= "cbe"

# def m1(self):
#     pass
# object = c1()
# object.m1()

#? Eg:5
# class c1:
#      def m1(self):
#          name "sid"
#          age = 28
    
#      def display(self):
#          # ! print(name, age)
#          # ! print(self, name, self,age)
#          print(self.m1())

#  object = c1()
#  object.display()

# c1 = class1()
# c1.dislay()

# ? Eg:6
# ? to use the variable inside the constructor in another methods
# class class1:
  # email = "sid@gmail.com"  #static variable
#     def _init__(self):   #instant variable
#        self.name "sid"
#        self.email = "sid@gmail.com"
       #return name, email #error ---> cannot use return with constructor

# def display(self):  # instant method
#     print(self.name, self.email)

# c1 class1()
# c1.display()

# ! --------> Inheritance
# the proccess of utilising the method and attributes of parent class
# thought the object of child class it is called as inheritance

# ? types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal inheritance

# Single Inheritance
# ? it has only one parent class and only one child class
# ! Eg:1
# class parent(child):
#     def m1(self):
#         print("iam parent class")

# class child:
#     def m2(self):
#         pirnt("iam child class")

# obj = child()
# obj.m1()

# ! Eg:2
# class c1:
#     def __init__(self):
#         print("iam constructor from parent class")

# class child (c1):
#     pass
# obj = child1()

# ! Eg:3
# class parent:
#     name = "sidhu"

# class child(parent):
#     name "name1"

#     def display(self):
#         print(self.name)

# d = child()
# d.display()

# ! Eg:4


# Eg:1
# class voice:
#     def sound(self):
#         print("All the animals have their own voices")
        
# class dog(voice):
#     def dog_voice(self):
#         print("bark")
        
# class cat(dog):
#     def cat_voice(self):
#         print("Meow")
        
# class parrot(cat):
#     def parrot_voice(self):
#         print("speak")

# all = parrot()
# all.dog_voice() # ==> bark
# all.cat_voice() # ==> Meow
# all.sound()      # ==> All the animals have their own voices
# all.parrot_voice() # ==> speak

# class honda_city:
#     def honda_city_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
#         print(cc, Hp, torque, fuel_type, num_of_piston)

#     def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
#         print(color, weight, height, length, vehicle_type)
# class amaze:
#     def_engine_specs(self, cc, Hp, torque, fuel type, num_of_piston):
#         print(cc, Hp, torque, fuel type, num of piston)
# class honda(civil)
#     def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
#         print(color, weight, height, length, vehicle_type
              
#     def amaze_engine_specs(self, cc, Hp, torque, fuel type, num_of_piston):
#         print(cc, Hp, torque, fuel type, num of piston)
#     def amaze_body_specs(self, color, weight, height, length, vehicle_type):
#         print(color, weight, height, length, vehicle_type)
# civic_engine_specs(self, cc, Hp, torque, fuel type, num_of_piston):
#     print(cc, Hp, torque, fuel type, num_of_piston)
# def civic_body_specs (self, color, weight, height, length, vehicle_type):
#     print(color, weight, height, length, vehicle_type).
I
# class Honda(civic):
#     pass

# honda Honda()
# honda.honda_city_engine_specs (1500, 230, 2979, "petrol", 4)
# honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback").

# eg:2
#class addition:
#     def add(self, a, b):
#         print(a+b)

#class subract:
#    def sub(self, a, b):
#        print(a-b)
        
#class multiply:
#    def mul(self, a, b):
#        print(a*b)
#        
#class division (addition, subract, multiply):
#    def div(self, a, b):
#        print(a/b)

#calc = division()
#calc.add(3, 4)
#calc.mul(5, 2)































































