# Creating a Class Called Calculator

class Calculator:

    # Constructor: Called when an object is created

    def __init__(self):
        print("Welcome to Python Calculator")
        print("*" * 30)

    # Function to take input numbers from users; only accepts digits

    def val_input(self):
        while True:

            try:
                # Prompt for input, accepting only digits

                self.num1 = int(input("Enter number: "))
                break

            except ValueError:
                print("Enter Digits for Desired Output")
                print("*" * 30)

        while True:
            try:
                # Prompt for input, accepting only digits
                
                self.num2 = int(input("Enter number: "))
                print("*" * 20)
                break

            except ValueError:
                print("Enter Digits for Desired Output")
                print("*" * 30)
    
    # Function for Addition

    def addition(self):
        return self.num1 + self.num2
    
    # Function for Subtraction

    def subtract(self):
        return self.num1 - self.num2

    # Function for Multiplication

    def multiply(self):
        return self.num1 * self.num2
    
    # Function for Division

    def division(self):

        # Using integer division to avoid float result

        return self.num1 // self.num2
    
# Create an instance of the Calculator class

obj = Calculator()

# Prompt user for operation choice

print("1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exit")
print("*" * 25)

while True:
    try:
        # Take operation choice from user; accept only digits

        choice = int(input("Enter your choice: "))
        print("*" * 25)
        if choice == 1:

            # Perform addition

            obj.val_input()
            print("Your sum is",obj.addition())
            
        elif choice == 2:

            # Perform Subtraction

            obj.val_input()
            print("Your subtraction is",obj.subtract())

        elif choice == 3:

            # Perform Multiplication

            obj.val_input()
            print("Your Multiplication is",obj.multiply())
        
        elif choice == 4:

            # Perform Division

            obj.val_input()

            # Using integer division to avoid float result

            print("Your Division is",obj.division())
        
        elif choice == 5:

            # Exit the program
            
            print("Thanks for using our Calculator app!")
            print("x" * 40)
            break

        else:
            print("Invalid Choice,try again")

    except ValueError:
        print("Enter Digits for Desired Output")
        print("*" * 35)

        

