person = {"name":"Alice", "age":25 ,"grade":"A"}

#add new key value pair 
person["address"]="l-38 HHC"

#update age

person["age"]= 32

print (person)

#remove 
if "grade" in person:
    del person["grade"]
    
print(person)