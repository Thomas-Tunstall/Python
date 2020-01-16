#1 Multiply Vectors

# listA = [2, 4, 5]
# listB = [2, 3, 6]
# listC = []

# listC = [a*b for a,b in zip(listA,listB)]

# print(listC)


#2 Matrix Addition

# listA = [ [1, 2], [3, 4]]
# listB = [ [1, 2], [3, 4]]
# listC = [[0, 0], [0, 0]]

# for i in range (len(listA)):
#     for l in range (len(listA[0])):
#         listC[i][l] = listA[i][l] + listB[i][l]
# print(listC)



#3 Matrix Addition II
# listA = [ [1, 2, 3], [3, 4, 5]]
# listB = [ [1, 2, 3], [3, 4, 5]]
# listC = [[0, 0, 0], [0, 0, 0]]

# for i in range (len(listA)):
#     for l in range (len(listA[0])):
#             listC[i][l] = listA[i][l] + listB[i][l]       
# print(listC)


# 4 De-dup
# a = [1,1,1,3,3,4,4,4,5,5,6]
# b = []

# b = list(dict.fromkeys(a))
# print(a)
# print(b)

# 5 Leetspeak

# s = ("I am a leet programmer").upper()

# leet = {'A' : '4', 'E' : '3', 'G' : '6', 'I' : '1', 'O' : '0', 'S' : '5', 'T' : '7'}

# for k, v in leet.items(): 
#     s = s.replace(k, v)

# print(s)

# 6 Long-long Vowels
# """I definitely did not do this right"""
# dark = ("aardvark")

# vowels = {'a' : 'aaaaa', 'e' : 'eeeee', 'i' : 'iiiii', 'o' : 'ooooo', 'u' : 'uuuuuu'}
# for a, v in vowels.items():
#     dark =dark.replace(a,v)

# print(dark)

"""A solution"""
# string_to_vowel_check = 'Good'
# last_letter = ''
# new_string = ''
# for letter in string_to_vowel_check:
#     is_vowel = False
#     if letter == last_letter:
#         if letter == 'a' or letter == 'A':
#             is_vowel = True
#         elif letter == 'e' or letter == 'E':
#             is_vowel = True
#         elif letter == 'i' or letter == 'I':
#             is_vowel = True
#         elif letter == 'o' or letter == 'O':
#             is_vowel = True
#         elif letter == 'u' or letter == 'U':
#             is_vowel = True
#     last_letter = letter
#     if is_vowel == True:
#         letter = letter*4
#     new_string+= letter
# print(new_string)



# # 7 The Caesar Cipher
# """I also did not do this one right, probably need to use a dictionary"""
# new = {'a': }
# cipher = ("lbh" + "zhfg" + "hayrnea" + "jung" + "lbh" + "unir" + "yrnearq")
# cipher_fix = "".join(chr(ord(letter)+13) for letter in cipher)
# print(cipher_fix)

txt = "lbh zhfg hayrnea jung lbh unir yrnearq" # message
alpha = "abcdefghijklmnopqrstuvwxyz"
offset = int(input("Please input offset number  "))
result = ""
for char in txt:
    # print(type(alpha.find(char)))
    if char in alpha:
        alpha_index = (alpha.find(char)-offset)%len(alpha)
        result = result + alpha[alpha_index]
    else:
        result = result + char
print(result)
