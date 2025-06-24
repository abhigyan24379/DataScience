import re  #module for regular expression 

#re.search(patter, string), re.findal(patter, string), re.sub(patter, replacement, string)

text = "Contact me at 123-456-7890"

#re.findall() method in Python helps us find all 
# pattern occurrences in a string. It's like searching 
# through a sentence to find every word that matches a 
# specific rule. We can do this using regular expressions 
# (regex) to create the pattern and then use re.findall()
# to get a list of matches.

digit = re.findall(r"\d+",text)
print (digit)

updated_text = re.sub(r"\d","x",text)
print(updated_text)
