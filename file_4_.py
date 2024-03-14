# ----> while loop
# ----> break using while loop

# Eg:1
# 1.) iterate from 20 to 30 and break the loop in 27

# i = 19
# while i <31:
#    if i ==27:
#        break
#    print(i)
#    i+-(i)
#    i+=1

#  2.
# i = 20
# while i<31:
#    print(i)
#    i+=1
#    if i==27:
#        break

# 3.)
# i = 20
# while i<31:
#   print(i)
#   if i==27:
#      break
    
# 4.)

# i=20
# while i<31:
#     if i==27:
#         print(i)
#         break
#     i+=1 # ===> 27
    
# -->continue

# i = 20
# while i<31:
#    i=i+1
#    if i==27:
#        continue
#    print(i)

# Eg:5
# while to iteratenfrom 12 to 22
# find the sum of all numbers

# i = 12
# sum=0
# while i<23:
#    sum=sum+i
#    print(sum)
#    i+=1
'''
# Eg :6
# find the average of value from 20 to 25

i = 20
sum=0
while i<26:
    sum=sum+i
    i+=1
    avg=(sum/6)
    print(avg)

i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)    

#--->nested for loop
#eg:1
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)

for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()
'''
# rows=int(input("enter the rows"))
# cols=int(input("enter the cols"))
      
# for row in range(rows):
#     for col in range(cols):
#         print("*", end=" ")
#     print()

sum=0
for row in range (5):
    for col in range(5):
        sum=sum+1 
        print(row, end=" ")
    print()    
# ======> 0 0 0 0 0 
#         1 1 1 1 1 
#         2 2 2 2 2 
#         3 3 3 3 3 
#         4 4 4 4 4 
 
#!  to print stars in right angled triangle


# for row in range(0, 50):
#     for col in range(0, row+1):
#         print("*", end=" ")
#     print()
    
# for row in range(6, 0, -1):
#     for col in range(0, row+1):
#        print("*", end=" ")
#     print()    

# for row in range(5):
#    for col in range(5):
#        if col==0 or col==5-1 or row ==0 or row ==5-1:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#            print()

for row in range(0,5):
    for col in range(0,6):
        if (row==0 and col==3) or (row==1 and(col>=2 and col<=4)or
                                (row==2 and (col>=1 and col<=5))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# ? ---> slicing
lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
#lst1[start_index:end_ index:step]

# print(lst1[0:4])
# print(lst1[6:8])
# print(lst1[3:6])
# print(lst1[:5])
# print(lst1[3:])
# print(lst1[:])

# print(lst1[0:7:1) # lst1[0:7]-->bothare same
# print(lst1[0:7:2])

# trai1 = int(input))


lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "1"]
# print(lst1[-4:-1])
# print(lst1[-1:-4])-->[]
# print(lst1[-7:-1])
# print(lst1[-7: 1:2])

# ! 



























    
