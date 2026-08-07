#by using if, elif, else  
first = input("ebter u r first no: ")
operator = input("enter operator (+, -, *, /, %) : ")
second = input("enter u r second no: ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
    
elif operator == "-":
    print(first - second)
    
elif operator == "*":
    print(first * second)
    
elif operator == "/":
    print(first / second)
    
elif operator == "%":
    print(first % second)
    
else:
    print("invalid operator")
    
