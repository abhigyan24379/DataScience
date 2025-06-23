first = "hello"
second = "world"
result = first +" " +second

# print (result)

text ="Python Programming"
# print (text[0:6])
# print (text[-11:])   # 11 letter from back 

name = "Alice"
age = 25 
print(f"my name is {name} and I am {age} years old.")

# split(), join(), replace(), strip()

sentence = "python,is,fun"
words = sentence.split(",")

new_sentence = " ".join(words)
print (new_sentence)

text = "I love java"
update_text = text.replace("java" , "python")
print(update_text)

messy = "   Hello, world   "
cleaned_text = messy.strip()
print (cleaned_text)