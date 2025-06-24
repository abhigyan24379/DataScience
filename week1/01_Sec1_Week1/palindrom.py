def is_palindrom (text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input("enter the string: ")
if is_palindrom(input_text):
    print (f"{input_text} is  a palindrom")
else:
    print(f"{input_text} is not a palindrom ")
    
    
    #search regex online and read and implement 
    