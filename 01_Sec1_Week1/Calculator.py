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