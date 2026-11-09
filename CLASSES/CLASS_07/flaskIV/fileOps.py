import pprint

# # Open rainbow.txt in append mode
# rainbowFile = open('files/rainbow.txt', "r")

# # read first 4 bytes (1 char per byte)
# out4 = rainbowFile.read(4)
# print(out4)

# # read all
# outAll = rainbowFile.read()
# print(outAll)

# # this one won't read anything because of the other reads()
# out_all_again = rainbowFile.read()
# print(out_all_again)

# # "bookmark" goes back to the beginning
# rainbowFile.seek(0)
# out_all_seek = rainbowFile.read()
# print(out_all_seek)

# # go back to beginning + reads one line
# rainbowFile.seek(0)
# oneLine = rainbowFile.readline()
# print(oneLine)

# # read all lines
# rainbowFile.seek(0)
# allLines = rainbowFile.readlines()
# print(allLines)
# pprint.pp(allLines[0])

# WRITING A TEXT FILE

# open / create file
sampleFile = open("files/sample_text_rev.txt", "w")

# input

# for i in range(3): 
#     a_name = input("Enter the name of the animal: ") 
#     sampleFile.write(a_name) 
#     sampleFile.write("\n") 
# sampleFile.close() 
# print("Data is written into the file.") 

# colorList = [] 
# for i in range(3): 
#     a_name = input("Enter the name of a color: ") 
#     colorList.append(a_name + '\n') 
# sampleFile.writelines(colorList) 
# sampleFile.close() 
# print("Data is written into the file.") 

# appending
sampleFile_a = open("files/sample_text.txt", "a")
nameList = [] 
for i in range(3): 
    a_name = input("Enter the name of someone in your class: ") 
    nameList.append(a_name + '\n') 
sampleFile_a.writelines(nameList) 
sampleFile_a.close() 
# print("Data is written into the file.") 




