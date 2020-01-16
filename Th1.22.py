# Short 1
# def name():
#     name = input("Name goes here ")
#     return name

# def subject():
#     subject = input("Subject goes here ")
#     return subject



# # print(f"{name()} favorite subject is {subject()}")

# # Short 2
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
def if_even():
    x = int(input("Is your # divisible by 2?"))
    if x / 2 == 1: #local vs global memory error??
        print("True")
    else:
        print("False")

if_even()







# # Medium
# """1. Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.
# It should return the smallest number in the List."""

# mylist = [1,2,3,4,5,6,7,8,9]

# def smallest():
#         print(smallest)