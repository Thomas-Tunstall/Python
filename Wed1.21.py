# #1 Multiply Vectors

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



# #3 Matrix Addition II
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
# # print(a)
# print(b)

# 5 Leetspeak

# replacements = [('a', '4'), ('e', '3',), ('g', '6'), ('i', '1'), ('o', '0'), ('s', '5'), ('t', '7')]

# s = ("I am a leet programmer")

# leet = {'a' : '4', 'e' : '3', 'g' : '6', 'i' : '1', 'o' : '0', 's' : '5', 't' : '7'}

# for k, v in leet.items(): 
#     s = s.replace(k, v)

# print(s)

# # 6 Long-long Vowels
# dark = ("aardvark")

# vowels = {'a' : 'aaaaa', 'e' : 'eeeee', 'i' : 'iiiii', 'o' : 'ooooo', 'u' : 'uuuuuu'}
# for a, v in vowels.items():
#     dark =c dark.replace(a,v)

# print(dark)

# 7 The Caesar Cipher
# cipher = ("lbh zhfg hayrnea jung lbh unir yrnearq")
# cipher_fix = "".join(chr(ord(letter)+1) for letter in cipher)
# print(cipher_fix)


