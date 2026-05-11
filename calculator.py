print("Welcome To Calculator!")
print("Pls Enter The Number first!")
try:

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Get Ready For Choose Your Operation")
    sign = {
            "1": "Addition",
            "2": "Subtraction",
            "3": "Multiplication",
            "4": "Division"

        }
    print(sign)
    while True:

        try:
            i = int(input("Enter The Operation Mentioned Numer Only:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if i == 1:
            print(f"The Result is {a} + {b} = ",a+b)
        
            
        elif i == 2:
            print(f"The Result is {a} - {b} = ",a-b)
            
        elif i == 3:
            print(f"The Result is {a} * {b} = ",a*b)
            
        elif i == 4:
            if b == 0:
                print("Cannot divide by zero")
            else:
                print(f"The Result is {a} / {b} = ",a/b)
        

        user = str(input("Enter Did You Want to continue(Yes/No):")).lower()
        if user == "no":
                break
except ValueError:
    print("Invalid input. Please enter a number.")


    
