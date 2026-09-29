class_professors ={'Cart_253_A': 'Pippin Bar',
                   'Cart_211': 'Brad Todd',
                   'Cart_214': 'Joanna Berzowska',
                   'Cart_215': 'Jonathan Lessard'}

specialList = {17: [1.6, 2.45], 
               42: [11.6, 19.4], 
               101: [0.123, 4.89]}

# print(type(specialList[17]))
# print(type(class_professors))
# print(class_professors["Cart_253_A"])
# print(specialList.keys())

# for key in specialList.keys():
#     print(specialList[key])

# print(specialList.values())

# for value in specialList.values():
#     print(value)

# for item in specialList.items():
#     print(type(item))
#     print(item[0])

# for item in specialList:
#     print(item)
#     print(specialList[item])

# shopping = {
#     'vegetables': [{'spinach':["green"]}', 'carrots', 'broccoli', 'lettuce'],
#     'fruit': ['canteloupe', 'bananas'],
#     'bakery': ['bagels', 'rye bread'],
# }

# print(type(shopping))
# print("Vegetable items on your list:")
# for item in shopping['vegetables']:
#     print("* " + item)

# print(shopping['vegetables'][0]['spinach'])

shopping_rev = {
    'vegetables': {"green": ["spinach", "broccoli", "lettuce"], "orange": ["carrots"]},
    'fruit': ['canteloupe', 'bananas'],
    'bakery': ['bagels', 'rye bread'],
}

shopping_rev["cleaning_items"] = ["dish-soap", "sponges"]
# print(shopping_rev)

shopping_rev["cleaning_items"].append("bleach")
print(type(shopping_rev))
