str1 = "adcb"
str2 = "acedb"

def myFun(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    lenstr1 = len(sorted_str1) 
    lenstr2 = len(sorted_str2)
    if lenstr2 > lenstr1:
        print(sorted_str2[lenstr2 - 1])

    

myFun(str1, str2)


