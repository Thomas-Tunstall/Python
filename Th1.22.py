# Short 1
# def name():
#     name = input("Name goes here ")
#     return name

# def subject():
#     subject = input("Subject goes here ")
#     return subject



# # print(f"{name()} favorite subject is {subject()}")

# Short 2
# def CtF():
#     C = int(input("Place the temperature here, in C "))
#     return (C * 9/5) + 32

# print(CtF())       

# # Short 3
# def FtC():
#     F = int(input("Place your temperature in F "))
#     return (F-32) * 5/9

# print(FtC())

#4 Short 4
# def if_even():
#     x = int(input("Is your # divisible by 2?"))
#     if x / 2 == 1:
#         print('True')
#         return True   
#     else:
#         print('False')
#         return False

# if_even()

#5 Short 5 Write an is_odd function that uses your is_even function to determine if a number is odd. 
# (That is, do not do the calculation - call a function that does the calculation.)
# Hint: You'll use the not keyword

# def if_even():
#     x = int(input("Pick a number, any number "))
#     if x % 2 == 1:
#         print('True')
#         return True   
#     else:
#         print('False')
#         return False

# def if_odd(if_even):
#     if if_even() == True:
#             print("Odd")
#     else:
#         if_even() == False
#         print("Even")

# if_odd(if_even)


#6 Only Evens

# only_evens = ([11, 20, 42, 97, 23, 10])

# def if_even(x):
#     for x in only_evens:
#         if x % 2 == 0: 
#             print("True")
#         else:
#             print("False")

# print(if_even(x))


# # Medium
# """1. Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.
# It should return the smallest number in the List."""

# Min
myList = [1,2,3,4,5,6,7,8,9]
number = min(myList)
print("the smallest is:", number)

# Max
myList = [1,2,3,4,5,6,7,8,9]
number = max(myList)
print("the smallest is:", number)

# # Strings Short
# strings = ["some", "example", "words", "that", "i", "am", "fond", "of"]
# print min(strings, key=len)

#Srings Long
strings = ["some", "example", "words", "that", "i", "am", "fond", "of"]
print max(strings, key=len)