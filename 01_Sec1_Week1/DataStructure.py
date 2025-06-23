
# #lists they are mutable 

# number = [1,2 ,3,4]
# fruits =["Apple", "Banana", "Orange"]

# mixed = [1, "Apple", True]

# # print(number[1])

# # print (fruits[2])

# # print(mixed[0])


# fruits.append("amrud")
# fruits.insert(1, "grapes")

# print(fruits)

# del fruits[0]

# # print (fruits)

# # fruits.pop()
# # print(fruits)

# sliced_fruits = fruits[1:3]
# print(sliced_fruits)


#tuple immutable 

# color = ("rede ", " green ", " blue")

# single_item = ("glass", )  # when we create a single tuple we have to place "," this in the end otherwise it will be an error 

# print (color[1])
# print (color[-1])

# print (single_item[0])

# print (color)



#dictoonary
# student = {"name ": "Alice", "age ": 25, "grade":"A" }

# print (student["name "])

# print(student["age "])
# print(student)
# student["subject"] = "Math"

# print(student)


# # del student ["grade"]
# # student.pop("subject")
# # print (student )

# for key,value in student.items(): # this keep everything in the list from the tuplee and we can access the items 
#     print(key,value)


#Sets unorder item of unique set

number = {1, 2, 3, 4}
empty_set = set()

print (number)
number.add(8)
print(number)
number.remove(2)
print(number)


set1 = {1,2,3}
set2 = {3, 4, 5}

print (set1 | set2)  #union operation bythe use of the pipe symbol "|"

print (set1 & set2) # in common 
print (set1 - set2) #difference 
