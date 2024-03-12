# a=7, 8
# print(a)
# print(type(a))

# a, b, c = 9, 8, 7, 8
# print(a, b, c)

# a, b=c=7, 8
# print(a)
# print(b)
# print(c)

# a=b, c=4, 2
# print(a, b, c)

# --->swapping of variable
# a = 7
# b = 5

# i=a
# a=b
# b=i
# print(a, b)

# eg:2
# a=a+b 
# b=a-b
# a=a-b

# print(a,b)

# eg:3
# a, b=b, a# only in python
# print(a,b)

# a=a*b #a=35
# b=a/b #b=36/7 =5.0
# a=a/b #a=35/5 =7.0
# print(int(a),int(b))

# id()----> used to find the memory address of the variable
# a=7
# b=8
# int(id(a))
# int(id(b))--># 2023701676464
               #2023701676496

# -->keywords
# -->key words are reserved words which provides speciale meaning to

# import keywords
# print(keyworld.kwlist)
# print(len(keyword.kwlist))
# print(type(keyword.kwlist))

# ---> to check if the srting is keyword or not
# print(keyword.is key("upi")==>false

# if = 8
# print(if)==>errors ocz is a keyword

# !--->literals
# literal is the constant value assigned to a varioble
# A variable is cosiders to be constant when if is defines in caps

# a=78 --> a is variable
# A=78-->A is constant

# hash() -- it creates a hash value for constant datatype and
# provides error for non constant datatypes
# n1 = 89+7j
# print(hash(n1))

# ! ----> operators
# ? operator are symbols which is used to perfeorm various operiour
# ? between 2 or more operands

# Arthimatic
# Assignment
# Logical
# Membership
# Bitwise
# Identify

# todo--->arthimatic  -->+, -, *, /, %, //, **
# eg:1
# a=8
# b=6
# c=9
# print(a+b+c)#==>23

# input() --> used to get the runtime input
# n1 = int(input("enter the value:"))
# print(type(n1))

# a=4
# b=2
# print(a/b) # is used to get the quotient value
# print(a%b) # is used  to gt the remainder value

# ! // -->floor devision operator

# a=7783679
# b=84
# print(a//b) # -> the output will be inn integer & the output will be
# based on floor value

#! ** --> used for power of a number
# print(2**4) # --> 16

# ! assignment --> +-=, -=, /=, *=, //=, **=, &=, |=

# a=8
# a+=2
# print(a)

# a=30
# a-=5
# print(a) # ==>39

#! comparision --> ==, >, <, !, <=, >=

# a=8
# b=6
# print(a=b0 # false

#! bitwise operator --> &, |,6, ~, <<, >>

# a=9
# b=7
# print(a&b) # ==> 4

# 2^4 2^3 2^2 2^1 2^0
#   8   4   2   1       

#   0   1   1   1 --->7
#   0   1   1   1 --->4 &
#  --------------------
#   0   1   0   0 --->3

# ~ --->
# a=5
# print(~a) # ==> -6 next -ve value

# <<,>>
# print(5<<3) # ==> 40
# print(5<<1) # ==> 2

#  logical
# and, or ,not
# a = 5
# print(a>3 and a<10) ==> true
# print(a>6 or a<10))
# print(not(a>8 and a<10))

#! Identity operator
# is, is not
#? it is used to compare the memory location that
# a-8
# b=6
# print(a is b)# ==>True
# print(a==b) # ==>True

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b) # ==> False

#! membership operator
# in, not in

# 11 = [7,8,9,0,5,7]
# num=55
# print(num in 11) # ==> false
# print(num not in 11) # ==>True

# num =678
# print(8 innum/0 # ==> error

# ! condition statement
# if, elif, else

# eg:1
# if (condition:  
# a=6
# if a>3:
#     print("hello")
# eg:2
# a=5
# if  a>3:
#     print("upi")
# else:
#     print("no")# ==> upi

# eg:3
# if a>8
# print("hello")
 
# else:
# print("no") # ==> no

# eg:4
# a =0
# a = none
# a=false
# a=""
# if a:
#    print("yes")
# else:
#    print("no") # ==> no

# sum:1
# a number is even or odd

# n = int(input("enter the number:"))
# if n %2==0:
#     print(n, "is even")


name=str(input("enter name"))
age=int(input("enter age"))
nationality =str(input("enter natinality")) 


if age>=21 and natinatity=="indian":
    print("eligible for vote")
else:
    print("not eligible")










      




























