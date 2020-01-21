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

your_string = "Make a string any string "
HoldingCell = {}

for keys in your_string:
    HoldingCell[keys] = HoldingCell.get(keys, 0) + 1

print ("Here's the count" + str(HoldingCell))


"""Med #2"""
# count = {}

# example = "I like cake"

# for i in example.split():
#     count[i] = len(i)

# print(count)

# myDict = {}
# word = print(input(str("Pick a word any word")))

# for i in word.split():
#     count[i] = len(i)

# print(myDict)       

"""Med 3"""
# 3. Sorting a histogram
# Please enter a sentence: To be or not to be do be do be do
# The top three words are:
# be: 4
# do: 3
# to: 2

your_string = "Make a string any string "
HoldingCell = {}

for keys in your_string:
    HoldingCell[keys] = HoldingCell.get(keys, 0) + 1
del HoldingCell[" "]

for key, value in sorted(HoldingCell.items()):
    print ("Here's the count  " + str(HoldingCell))

for keys in HoldingCell(keys, 0):
    if len(keys) > 3:
        append.HoldingCell(keys, value)