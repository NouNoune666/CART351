# print(len("A good day is one with lots of ice cream!"))

# print(len("camembert") + len("cheddar"))

# print("ice" in "ice cream")
# # or:
# print("vanilla" in "ice cream")

# print("ice cream".startswith("ice"))
# print("ice cream".endswith("ice"))

# print("ice cream".startswith("ice"))
# print("ice cream".endswith("ice"))

# print("ice".isdigit())
# print("25690".isdigit())
# print("25690.89".isdigit())

# print("ice cream".islower())
# print("Ice cream".islower())
# print("ICE cream".isupper())
# print("ICE CREAM".isupper())

# choccy = "I love chocolate especially with nuts"
# choccychocc = "I love chocolate especially chocolate with nuts"

# print(choccy.find("choc"))
# print(choccy.find("nutty"))
# print(choccychocc.find("choc"))

# print(choccy.count("choc"))
# print(choccy.count("nutty"))
# print(choccychocc.count("choc"))

# print("west" == "east")
# print("east" == "east")
# print("WEST" == "West")

# upper()
# This function will return the string all in upper case:
# allInUpper = "questions! and Anwsers and more questions!".upper()
# print(allInUpper)

# allInLower = "questions! and Anwsers and more questions!".lower()
# print(allInLower)

# capitalizeEach = "questions! and Anwsers and more questions!".title()
# print(capitalizeEach)

# print(" got some space at beginning and at end. ")
# removeWhite = " got some space at beginning and at end. ".strip()
# print(removeWhite)

# originalText = "I love ice cream and cookies and I love carrots and bananas but what I love most is lasagna"
# replaceAll = originalText.replace("I love", "I dislike", 1)
# print(replaceAll)

# # lists
# fruits = ["oranges", "bananas", "melons", "strawberries"]
# vegetables = ["carrots", "aubergines", "celery", "cauliflower"]
# mixed_bag = [1, 3, "nothing", 2.4, True]

# for el in fruits:
#     print(f"I love {el}")

# testString = "A wonderful sunshiny day"
# for ch in testString:
#     print(ch)

# # empty list
# newItems = []
# newItems.append("first")

# # append using a for loop:
# for i in range(2, 10):  # i is between 2 and 10
#     newItems.append(f"{i} is the next item")

# for el in newItems:
#     print(el)

# var_A = 34
# things = ['cat', 'pencil', 34, True, -164, "whale", var_A]

# print(things[0])
# print(len(things))

# anotherTest = "A wonderful rainy day"
# print(f"character at position 0 (1st) {anotherTest[0]}")
# print(f"character at position 2 (3rd) {anotherTest[2]}")

# # INSERT
# testList = ["abc", "3", 56, 67, True, ["a", "b", "c"]]
# testList.insert(2, "new element")  # insert in 3rd place
# for el in testList:
#     print(el)

# # EXTEND

# listA = ["red", "blue", "orange"]
# listB = ['sarah', 'michael', 'kiara', 'stephen']
# listA.extend(listB)
# print(listA)

# listC = ['cats', 'dogs', 'parrots']
# listA += listC
# print(listA)

# # 1
# aL = ["1", "2"]
# bL = ["a", "c", "b"]
# cL = aL + bL
# print(cL)

# # 2
# dL = aL + aL + bL
# print(dL)

# listQ = ['cats', 'dogs', 'parrots']
# # print(listQ.index("Cats"))  # will throw a Value Error and ends program
# print(listQ.index("cats"))

# # on strings
# myStringTest = "another fine snowy day"
# # print(myStringTest.index("z"))  # will throw a Value Error and ends program
# print(myStringTest.index("s"))

# listToSort = ['water', 'question', 'apples', 'wander']
# listToSortBools = [True, True, False, True]
# listToSortNums = [2.5, 6, 7, 43, 102.6, 1, 1.2, 0.8]

# print(f"before:: {listToSort}")
# listToSort.sort()
# print(f"after:: {listToSort}")

# print(f"before:: {listToSortBools}")
# listToSortBools.sort()
# print(f"after:: {listToSortBools}")

# print(f"before:: {listToSortNums}")
# listToSortNums.sort()
# print(f"after:: {listToSortNums}")

# el = listToSort.pop()  # take out at end
# print(f"item removed: {el}")
# print(f"rev list: {listToSort}")

# strTest = "what a super day"
# if 'p' in strTest:
#     print("found p")
# if 'what' in strTest:
#     print("found what")
# if ' ' in strTest:
#     print("found space")
# if 'days' in strTest:
#     print("found days")
# else:
#     print("not in")

# element_list = ["hydrogen", "helium", "lithium", "beryllium", "boron"]
# glue = ", and "
# single_str = glue.join(element_list)
# print(single_str)

# single_str.split()
# print(single_str.split())

# qList = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
# qList[0:2] = 'z'  # replace [1,2] with single ['z']
# print(qList)

# rList = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
# rList[0:2] = 'zz'  # replace [1,2] with ['z','z']
# print(rList)

# sList = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
# sList[4:-1] = 'nnn'  # replace
# print(sList)


# newItems = []
# newItems.append("first")

# print(newItems)
# print(len(newItems))

# listA = ["red", "blue", "orange"]
# listB = ['sarah', 'michael', 'kiara', 'stephen']
# listA.extend(listB)
# print(listA)
# listB.extend(listA)
# print(listB)

# listC = ["cats", "dogs", "parrots"]
# listA = listC
# print(listA)

# listToSort = ['water', 'question', 'apples', 'wander']
# print(listToSort)
# listToSortBools = [True, True, False, True]
# listToSortNums = [2.5, 6, 7, 43, 102.6, 1, 1.2, 0.8]

# listToSort.sort()
# print(listToSort)
# listToSort.reverse()
# print(listToSort)

# listToSort.pop()
# print(listToSort)

# if "question" in listToSort:
#     print("yes")
# if "question" not in listToSort:
#     print("no")

# qList = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
# qList[0:2] = 'zzz'  # replace [1,2] with single ['z']
# print(qList)

franken_1 = open("data/frankenstein.txt").read()
print(franken_1)