import re
def clean_text(text):
    #remove punctuation
    text = re.sub(r"[^\w\s]","",text)
    #remove extra spaces
    text = " ".join(text.split())
    #convert to lower space
    return text.lower()

input_text = "   hello dear how do you do !!!!  Programming Python"
cleaned_text = clean_text(input_text)
print("cleaned text is : ", cleaned_text)

