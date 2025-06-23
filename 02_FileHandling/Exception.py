#why use Exception Handling  for files operation 

# prevents the programs from crashing due to the file-related errors (e.g. file not found )

#using try except blocks 



try:
    with open("e:/pythonAi/02 FileHandling/sample.txt", "r") as file:
        content = file.read()
except:
    print ("file not found")