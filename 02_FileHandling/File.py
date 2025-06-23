with open("e:/pythonAi/02 FileHandling/sample.txt", "w") as file:
    # content = file.read()
    # print (content)
    file.write("hey abhigyan how are you ")
    file.writelines(["Alice", "Bob", "Cherry"])
    # content = file.read()
    # print(content)
    
#file is automatically closed when we use with keyword
# With ensures files are properly closed after operation, even if an exception occurs
#advantage 
# 1) simplifies code 
# 2) reduces the risk of the file corruption 



# import os 
# print("current working folder ", os.getcwd())
