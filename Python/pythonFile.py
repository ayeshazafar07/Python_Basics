# # To run script- type on terminal 
# # python filename.py
# print("hello world")

# # pyjokes is a module that gives you jokes when run
# # pip install pyjokes
# import pyjokes
# joke = pyjokes.get_joke()
# print(joke)

# # Input function
# a = input("Enter any number ")
# b = input("Enter any number ")

# print("Input number is: ", a)
# print("Input number is: ", b)
# print("Sum of numbers is: ", a+b) # will give concatenated output

# print("Sum of numbers is: ", int(a)+int(b)) # will give integar sum

# # to use variable inside string use f string
# p = input("enter your name: ")
# print(f"Good Afternoon {p}") 
# # another way is 
# # print("Good Afternoon " + p) 

# # customize string
# letter = '''
# Dear <|name|>,
# You are selected!
# <|Date|>
# '''
# print(letter.replace("<|name|>", p).replace("<|Date|>", "24/11/25"))

# # detect double space
# q = "i dont have  any patience"
# print(q.find("  ")) # we created substring of double space

# # replace double space
# q = "i dont have  any patience"
# print(q.replace("  "," ")) # we created substring of double space

# #list of 3 fruits given by user
# my_list = []
# f1 = input("Fruit? ")
# my_list.append(f1)
# f1 = input("Fruit? ")
# my_list.append(f1)
# f1 = input("Fruit? ")
# my_list.append(f1)

# print(my_list)

# # sum list items
# l5 = [1,2,3,4]
# print(sum(l5))


# # dictory to give meaning of urdu to english
# words = {
#     "billi": "cat",
#     "kursi": "chair",
#     "madad": "help"
# }
# word = input("enter word you want meaning of: ")
# print(words.get(word))

# #take 8 numbers and print all unique
# set1 = set()
# num = int(input("enter number 1: "))
# set1.add(num)
# num = int(input("enter number 2: "))
# set1.add(num)
# num = int(input("enter number 3: "))
# set1.add(num)
# num = int(input("enter number 4: "))
# set1.add(num)
# num = int(input("enter number 5: "))
# set1.add(num)
# num = int(input("enter number 6: "))
# set1.add(num)
# num = int(input("enter number 7: "))
# set1.add(num)
# num = int(input("enter number 8: "))
# set1.add(num)

# print(set1)

# # different data types are unique in set
# s = set()
# s.add(17)
# s.add("17")

# print(s)


# # different data types are unique in set
# # but when floating point is same number then it is integar
# # 1 == 1.0 is True
# # 1 == 1.8 is False
# # so 20 and 20.0 are same for set but 20 and 20.4 are different 
# s = set()
# s.add(20)
# s.add(20.0)
# s.add(20.4)
# s.add("20")

# print(s)

# # dictionary of frinds name and fav languages
# favLang = {}
# name = input("Friend 1 name: ")
# language = input("Friend 1 fav language: ")
# favLang.update({name: language})
# name = input("Friend 2 name: ")
# language = input("Friend 2 fav language: ")
# favLang.update({name: language})
# name = input("Friend 3 name: ")
# language = input("Friend 3 fav language: ")
# favLang.update({name: language})
# name = input("Friend 4 name: ")
# language = input("Friend 4 fav language: ")
# favLang.update({name: language})
# name = input("Friend 5 name: ")
# language = input("Friend 5 fav language: ")
# favLang.update({name: language})

# print(favLang)

# marks = {
#     "stuA": 100,
#     "stuB": 50,
#     "stuC": 75
# }
# marks.update({"stuA": 98})
# print(marks)
# marks.update({"stuX":50})
# print(marks)

# # print if age even
# age = int(input("enter your age: "))
# if(age%2==0):
#     print("even age")
# elif(age%3==0):
#     print("age multiple of 3")
# else:
#     print("puufff")

# # spam message detector
# p1 = "buy now"
# p2 = "subscribe this"
# p3 = "click this"

# message = input("enter message: ")

# if((p1 in message) or (p2 in message) or (p3 in message)):
#     print("this is spam message")
# else:
#     print("not spam")


# # Multiplication table of 7
# for i in range(1, 71):
#     if(i % 7 == 0):
#         print(i)

# n = int(input("enter number "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# n = int(input("enter number "))
# i = 0
# while(i<11):
#     print(f"{n} x {i} = {n * i}")
#     i+=1


# # greet those whose name starts with s
# l1 = ["Harry", "Shubham", "Sachin", "Rahul"]
# for i in l1:
#     if(i.startswith("S")):
#         print(f"Hello {i}")


# # prime number or not
# n = int(input("enter number "))
# for i in range(2, n):
#     if((n % i) == 0):
#         print("Not prime")
#         break
# else:
#     print("Prime")


# # Factorial of number
# # 5! = 1 x 2 x 3 x 4 x 5
# n = int(input("enter number "))
# product = 1
# for i in range(1, n+1):
#     product = product * i
# print(f"Factorial of {n} is {product}")


# # print * pattern
# '''
#   *
#  ***
# *****
# ''' 
# n = int(input("enter number "))

# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")


# '''
# *
# **
# ***
# '''
# n = int(input("enter number "))
# for i in range(1, n+1):
#     print("*"*i, end="")
#     print("")

# '''
# ***
# * *
# ***
# '''
# n = int(input("enter number "))
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"*n, end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

# # Multiplication table in reverse order
# n = int(input("enter number "))
# for i in range(1,11):
#     print(f"{n} x {11-i} = {n*(11-i)}")


# # recursion to sum first n natural numbers
# # 5 = 5 + 4 + 3 + 2 + 1

# def sum(n):
#     if(n==1):
#         return 1
#     return n + sum(n-1)

# num = int(input("enter number "))
# print(sum(num))

# '''
# ***
# **
# *

# with recursion
# '''
# def star(n):
#     if(n==0):
#         return
#     print("*" * n)
#     star(n-1)

# num = int(input("enter number "))
# star(num)

# # storing highscore and updating in file
# import random

# def game():
#     score = random.randint(1,100)
#     # fetch high score from file
#     with open("highscore.txt") as f:
#         highscore = f.read()
#         if(highscore!=""):
#             highscore = int(highscore)
#         else:
#             highscore = 0
#     print(f"score is {score}")
#     if(score>highscore):
#         with open("highscore.txt", 'w') as f:
#             f.write(str(score))

# game()

# # sensor words in file
# words = ["donkey", "bad", "good"]

# with open("file2.txt", 'r') as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "#"*len(word))

# with open("file2.txt", 'w') as f:
#     f.write(content)

# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p1 = Programmer("Harry", 1200, 123456)
# print(p1.company, p1.name, p1.salary, p1.pin)

# p2 = Programmer("Abc", 2300, 567894)
# print(p2.company, p2.name, p2.salary, p2.pin)


# class Calculator:
#     def __init__(self, num):
#         self.num = num

#     def square(self):
#         print(f"Square of {self.num} is: {self.num*self.num}")

#     def squareRoot(self):
#         print(f"Square Root of {self.num} is: {self.num**1/2}")

#     def cube(self):
#         print(f"Cube of {self.num} is: {self.num*self.num*self.num}")

# n1 = Calculator(4)
# n1.square()
# n1.squareRoot() 
# n1.cube()

# from random import randint
# class Train:
#     def __init__(self, trainNo):
#         self.trainNo = trainNo

#     def book(self, trainFrom, trainTo):
#         print(f"Ticket is booked in train no {self.trainNo} from {trainFrom} to {trainTo}")
    
#     def getStatus(self):
#         print(f"Train {self.trainNo} is on time")

#     def getFare(self, trainFrom, trainTo):
#         print(f"Price of train no {self.trainNo} from {trainFrom} to {trainTo} is: {randint(200,500)}")

# t1 = Train(12345)
# t1.book("Isb", "Lhr")
# t1.getStatus()
# t1.getFare("Isb", "Lhr")


# class Employee:
#     salary = 234
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         print(1)
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         print(2)
#         self.increment = ((salary/self.salary) -1) * 100

# e = Employee()
# e.salaryAfterIncrement = 280.8 # calls @salaryAfterIncrement.setter
# print(e.salary) # class salary that is already stored either by class or instance attribute
# print(e.salaryAfterIncrement) # calls @property
# print(e.increment) # calls newly set increment attribute


# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self, c2):
#         return Complex(self.real + c2.real, self.imag + c2.imag)
#     # if you dont use str conversion then output will be like 
#     # <__main__.Complex object at 0x000001AAB5EAB0B0>
#     def __str__(self):
#         return f"{self.real} + {self.imag}i"

# c1 = Complex(1, 2)
# c2 = Complex(3, 4)

# print(c1 + c2)


# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result
    
#     def __mul__(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result
    
#     def __str__(self):
#         return f"{self.x}i + {self.y}j + {self.z}k"

# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)
# print(v1 + v2)
# print(v1 * v3)


# class VectorLength:
#     def __init__(self, l):
#         self.l = l

#     def __len__(self):
#         return len(self.l)

# v1 = VectorLength([1, 2, 3])
# print(len(v1))


# Exception Handling
# try: 
#     a = int(input("Enter a number: ")) # we have specified int but user can enter string which would result in error so we need to handle it
#     print(a)
# except Exception as e:
#     print(e)


# table using list comprehension
# n = 5
# table = [n*i for i in range(1,11)]
# print(table)
