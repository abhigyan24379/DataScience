print("hello")

#define  variable fof different type 
# integer_var = 10 
# float_var = 3.14
# string_var = "ai"
# list_var = [1,2,3]
# tuple_var = (4,5,6 )
# dict_var = {"name":"Alice" , "role":"Engineer"}
# bool_var = True

#print and manipulate 

# print ("Integer : ",integer_var)
# print("Float : ", float_var)
# print("String : ", string_var +"bootcamp" )
# print("List : ", list_var)
# print("Tuple :", tuple_var)
# print("Dict :" , dict_var)
# print("Boolean : ", bool_var)

#control flow in python 


# num = 10 
# if num > 0:
#     print("Positive number ")
# elif num == 0:
#     print("its a zero")
# else:
#     print("its a negative number ")
    
#Nested condition

# age = 25 
# if age > 18 :
#     if age <30:
#         print ("young adult")
#     else:
#         print("adult")
        
#loops
#loop through the list of the items 

# fruits = ["apple", "banana","cherry "]
# for fruit in fruits :
#     print (fruit)
    
    
#loop with range 
# for i in range(5):
#     print(i)

#while
# count = 5
# while count >0:
#     print(count)
#     count -=1


#prime number :

num = int(input("Enter a numnber : "))

if num > 1:
    for i in range (2, int (num ** 0.5)+1):
        if num % i == 0:
            print(f"{num} is not a prime ")
            break
        else :
            print(f"{num } is a prime number ")
else: 
    print(f"{num } is not a prime number ")
    
def add(a,b ):
    return a+b

def subtract(a, b ):
    return a - b 

def multiply (a, b ):
    return a * b

def div(a,b):
    if b != 0 :
        return a / b
    else : 
        return "division by zero is not allowed "
    
while True:
    print ("\nMenu:")
    print("1. Add")
    print ("2. Sub")
    print("3. Multi")
    print ("4. Div")
    print ("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice =="5":
        print ("Exitng the program ")
        break
    
    num1 = float(input("Enter first nmber: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        print("Result: ", add(num1, num2))
    elif choice == "2":
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        print("Result: ", div(num1, num2))
    else:
        print("Invalide choice. Please try again.")