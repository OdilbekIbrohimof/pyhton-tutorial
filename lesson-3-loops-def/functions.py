# def funksiya nomi :
#   funksiya tanasi

# import re
# def plus(x, y):
#   return x + y
# print(plus(1 , 2)) # 3

# task 1
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# def max(x , y):
#   if x > y :
#     return "Birinchi son katta"
#   else :
#     return "Ikkinchi son katta"
# print(max(a , b))

# task 2
# def kvadrat(x):
#   print(x ** 2 , end=' ')
# for i in range(1 ,11):
#   print(kvadrat(i))

# def main(x):
#   a = 10 # local variable
#   return x
# print(a) # Error

# def main(x):
#   global a
#   a = 10 #global
#   return x
# print(a + 2) # 12

# positsanal argument
# def main(name):
#   return name
# TypeError: main missing 1 required positional argumanet : 'name'
# print(main())

# no positsanal argument
# def main(name=None , surname=None , position="worker"):
#   return f"{name} {surname} {position}"
# print(main()) # None None "worker"
# print(main("john")) # "john" , None , "worker"
# print(main("john" , "doe" , "staff")) #  "john" , "doe" , "staf"
# print(main("john" , "doe")) #  "john" , "doe" , "worker"

# task 3
# def user(name=None , surname=None , position="worker" , age=None , idcard="Metirka"):
#   return f"{name} {surname} {position} {age} {idcard}"
# print(user("Odilbek" , "Ibrohimov" , "Student" , None , 15))

# task 4
# a = int(input("son kiriting"))
# def num(x=50):
#   for i in range(1 ,  x , 2):
#     print(i)
# num(a)