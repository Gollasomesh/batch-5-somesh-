# ! Eg:3
# ? take value of length and breadth of a
# ? from user and check if it is square or not

# length =  int(input())
# breadth = int(input())
# if length--breadth:
#    print("its a square")
# else:
#    print("its not square"

# ! Eg:4
# python program to chech wheather the
# give integer is a multiple of both 5 and 7

# n = int(input("enter the number:")
# if n%5==0 and n%7==0:
#         print("yes")
# else:        
#      print("no")

# ! Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria :

#     cost price (in Rs)                     Tax
#     >100000                                15 % + discount 6%
#     >50000 and <=100000                    10%
#     <= 50000                               5%

# price = int(input("enter the price:"))
# total = 0
# if price>=100000:
#     discout = price*(6/100)
#     value = price-discount
#     amount = value*(15/100)
#     print=value + amount

# else:
#   tax = price*(5/100)
#     total = price+tax
# print("The onroad cost of bike is: ",total)    


# if clif
# Eg:1
# a=7
# b=9
# c=3

# if a>b and a>c:
#  elif b>a and b>c:
#     print("b is greater")
# elif:
#   print("c is greater")

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. above 80 - A
# Ask user to enter marks and print the correspnding grade.

# mark = int(input("Enter mark:"))
# if mark>=80 and mark<=100:
#    print("A")
# elif mark>60 and mark<80:
#    print("B")
# elif mark>=50 and mark<60:
#    print("C")
# elif mark >=40 and mark<50:    
#    print("D")
# elif:
#   print("fail")

# ! Eg:6
# ? accept the age of 4 people and display the oldest one.

# ! --> short hand if else
# Eg:1
# a=9
# b=60
# if a>b:
#    print("A")
# else:
#      print("B")
# ? --> using short hand if else
# * Rules
# 1.) statement the inside the if condition have tobe present at first
# 2.) elif cannot be used in short if else
# 3.)aiways it have to end with else

# print("A")if a>b else print("B")

# ! code to check the given char is vowel or consonent
# char = input("Enter the char:")
# if char=="a" or char 'e' or char =='i' or char =='o' or char =='u':
# print("is a vowel")
# else:
#     print("its consonent")

# ? or

# strl = "aeiouAFIOU"
# if char in str1:
#      print("vowl")
# else:
#     print("consonnt")
          
# ! shorthand if else
# char = input("enter the char:")
# str1 = "aeiouAEIOU"
# print("vowe") if char in str1 else("consonent")

# ! ----> elif ladder using short hand if else
# Eg:1
# ? Find greater among 3 variables using short hand if else
# a=8
# b=5
# c=9

# print("A is greater") if a>b and b>c else print("B is greater")
# if b>a and b>c else print("C is greater")

# ! -----------> looping

# looping can be implemented using
# for loop
# while loop

# ---> for loop
# ? for loop is used for iteartion, if we know the number of times the loop have to run 
# ? it is used to iterate the iterable eg(string, list, tuple, etc...)

# todo --> syntax for loop

# ! for syntax in c
# for(i=0;1<10;1++){
#     printf("hello");
# }

# ! for syntax in python
# for userdefined_variable in range(start, end,step): default step value is 1
#     statement
#     statement
#     statement

# ? Eg:1
# To print the value from 1 to 10 using for loop

# for 1 in range(0,10): #(n , n-1)
#     #  print(i)
#     print("hello")

# ? Eg:2
# for val in range(23,50,5):
#     print(val)

# for val in range(1, 15, 3):
#     print(val)

# Eg:3
# to decrement the value

# for val in range(10, 0, -1):
#     print(val)

# Eg:4
# print the output of 7th multiplecation table from 21 to 43
# for val in range (1, 1000+1):
#    print('jai sree ram ',val*8  

# --> method :2

# ans="7 x () = {}"
#    print(ans.format(val, val*7))

#   --> method:3
#    print(f"7 x {val}={val*7}")

# ?Eg:5
#break --> used to terminate the loop

# for val in range(1, 100):
#    if val ==99:
#        break
#    print(val*10)

# Eg:6
# for val in range(1,100):
#     if val ==99:
#        print(val)
#        break

# ! continue
# Eg:1
# for val in range(1, 10):
#    if val ==6:
#        continue
#    print(val)

# for val in range(2, 30,):
#      if val ==6 or val ==8 or val ==21:
#         continue
#      print(val)

# ! prtactise problem    
# ? print the even number between 20 to 100
# for val in range(20, 41):
#    if val %2==0:
#        print(val)

# ! ---------> while loop
# ? while is used when we do not know the number of times the loop have to run 
# ? to iterate the non iterable elements while loop is used

# todo syntax

# initialisation
# while condition:
#     statement
#     incre or decre

# ! Eg:1
# to iterate numbedr from 1 to 10

# i = 0
# while i<11:
#     print(i)

# for loop practisee
# write aprogram to display sum of odd number and even
# numbers that fall between
# 12 and  37(including both numbers)

# Eg:2
# to decrement  using while loop
# i=10
# while i>0:
#     print(i)
#     i-=1



























'''
# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432

























    
