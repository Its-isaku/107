
#? calculator

#? Mini challenge -> create a calculator that takes two umbers, use this operators (+, -, *, /) and return the result

def menu():
    print("|-------Welcome to the calculator-------|")
    print("| 1 -> Add                              |")
    print("| 2 -> Subtract                         |")
    print("| 3 -> Multiply                         |")
    print("| 4 -> Divide                           |")
    print("| 5 -> Exit                             |")
    print("|----------------------------------------|")
    
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def getInput():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a, b

def main():
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a, b = getInput()
        print(f"{a} + {b} = {add(a, b)}")
        print("\n")
        
    elif choice == 2:
        a, b = getInput()
        print(f"{a} - {b} = {subtract(a, b)}")
        print("\n")

    elif choice == 3:
        a, b = getInput()
        print(f"{a} * {b} = {multiply(a, b)}")   
        print("\n")
        
    elif choice == 4:
        a, b = getInput()
        print(f"{a} / {b} = {divide(a, b)}" if b != 0 else "Error: Division by zero")
        print("\n")
    
    elif choice == 5:
        print("Exiting...")
        print("\n")
        exit()
        
    else:
        print("Invalid choice")
        print("\n")

if __name__ == "__main__":
    while True:
        main()