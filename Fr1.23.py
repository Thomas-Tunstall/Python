"""Short #1"""

# phonebook_dict = {
# 'Alice': '703-493-1834',
# 'Bob': '857-384-1234',
# 'Elizabeth': '484-584-2923'
# }

# print(phonebook_dict["Elizabeth"])
# phonebook_dict ["Kareem"] = "938-489-1234"
# del phonebook_dict["Alice"]
# phonebook_dict['Bob'] = "968-345-2345"
# values_list = phonebook_dict.values()
# print(values_list)

# print(phonebook_dict)

"""Med #1"""
# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

# your_string = input("Make a string any string ")
# HoldingCell = {}

# for keys in your_string:
#     HoldingCell[keys] = HoldingCell.get(keys, 0) + 1

# print ("Here's the count" + str(HoldingCell))


"""Another Example"""
# word = input("Word here")
# empty_dict = {}

# for letters in word:
#     if letters not in empty_dict:
#         empty_dict[letters] = 0
#     empty_dict[letters] += 1
# print (empty_dict)

"""
for char in word:
    if char not in dict:
        dict[char] = 0
    dict + char += 1     

"""

"""" for char in word:
   if char not in dict
       dict[char] = 1
   else dict + char = dict + [char] + 1"""

"""Med #2"""
# count = {}

# example = input("Put a string here")

# for i in example.split():
#     count[i] = len(i)

# print(count)    

"""Med 3"""
"""# 3. Sorting a histogram
# Please enter a sentence: To be or not to be do be do be do
# The top three words are:
# be: 4
# do: 3
# to: 2"""

# your_string = "Make a string any string "
# HoldingCell = {}

# for keys in your_string:
#     HoldingCell[keys] = HoldingCell.get(keys, 0) + 1
# del HoldingCell[" "]

# for key, value in sorted(HoldingCell.items()):
#     if len(keys) > 3:
#         HoldingCell.append(keys, value)
#     elif len(keys) = 3:
#         print(HoldingCell)


LC = {}
word = input(‘Please enter a word to count top 3 letters: ’)
# word=‘hellllooooooohahahhhhh’
for l in word:
    if l in LC:
        LC[l] = LC[l]+1
    else:
        LC[l] = 1
top_list=[[“”,0],[“”,0],[“”,0]]
for k, v in LC.items():
    if v > top_list[0][1]:
        top_list[2][0]=top_list[1][0]
        top_list[2][1]=top_list[1][1]
        top_list[1][0]=top_list[0][0]
        top_list[1][1]=top_list[0][1]
        top_list[0][0]=k
        top_list[0][1]=v
    elif v > top_list[1][1]:
        top_list[2][0]=top_list[1][0]
        top_list[2][1]=top_list[1][1]
        top_list[1][0]=k
        top_list[1][1]=v
    elif v > top_list[2][1]:
        top_list[2][0]=k
        top_list[2][1]=v
print(top_list)


# print ("Here's the count  " + str(HoldingCell))