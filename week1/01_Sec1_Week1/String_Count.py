sentence = input("enter a sentence")


#split the sentence into words

words = sentence.split()

# Initialize dictonary 
word_count = {}

#count the word frequence
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print (word_count)
    