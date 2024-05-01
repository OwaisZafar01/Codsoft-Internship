# Import the random module

import random

# Create a class called Password

class Password:
    
    # Assign variables for alphabets, digits, and special characters

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "123456789"
    special_characters = "!@#$%^&*()_+"

    # Create a Constructor when object is created

    def __init__(self):
        print("Welcome to Password Generator App")
        print("*" * 35)

    # Print complexity options for Users  

    def complexity(self):

        print("""1: Strong Password, It contaings Alphabets,digits and Special Characters
2: Good Password, It contains Alphabets and digits
3: Fair Password, It contains Alphabets
4: Poor Password, It contains Digit
5: Exit""")
        print("*" * 65)

    # Add Digits,Alphabets and Special Characters for strong Password
    strong_password_generator = alpha + digits + special_characters

    # Add Digits and Alphabets for Good Password
    Good_password_generator = alpha + digits

    # Add Alphabets for Fair Password
    fair_password_generator = alpha

    # # Add Digits for Poor Password
    poor_password_generator = digits

    # Take Input Password Length

    def password_length(self):
        while True:
            try:

                # Prompt the user to enter password length
                
                self.pass_length = int(input("Enter Password Length: "))
                print("*" * 28)
                if (self.pass_length >= 8) and (self.pass_length <= 20):
                    break

                else:
                    print("Password Length must be Between 8 to 20")
                    print("*" * 25)

            except ValueError:
                print("Only Digits are Allowed")
                print("*" * 25)
                continue  

    # Generate Strong Password 

    def strong_password(self):
        self.alphabets = random.choice(self.alpha)
        self.numbers = random.choice(self.digits)
        self.spec_characters = random.choice(self.special_characters)

        self.final_password = self.alphabets + self.numbers + self.spec_characters
        self.updated_length = self.pass_length -3
        self.final_password += "".join(random.choice(self.strong_password_generator) for i in range(self.updated_length))

        return self.final_password

    # Generate Good Password 

    def good_password(self):
        self.characters = random.choice(self.alpha)
        self.num = random.choice(self.digits)

        self.final_pass = self.characters + self.num
        self.remaining_length = self.pass_length - 3
        self.final_pass += "".join(random.choice(self.Good_password_generator) for i in range(self.remaining_length))

        return self.final_pass

    # Generate Fair Password

    def fair_password(self):
        return "".join(random.choice(self.fair_password_generator) for i in range(self.pass_length))
    
    # Generate Poor Password

    def poor_password(self):
        return "".join(random.choice(self.poor_password_generator) for i in range(self.pass_length))
    

# Create an instance of the Password class

obj = Password()

# Get password length from the user

obj.password_length()

# Display complexity options for user

obj.complexity()

# Ask for user's choice of password complexity

while True:
    try:
        
        ask_complexity = int(input("Enter your choice: "))
        print("*" * 25)
        if ask_complexity == 1:

            # Generate Strong Password

            print(obj.strong_password())
     
        elif ask_complexity == 2:

            # Generate Good Password

            print(obj.good_password())
         
        elif ask_complexity == 3:

            # Generate Fair Password

            print(obj.fair_password())
     
        elif ask_complexity == 4:
            
            # Generate Poor Password
            
            print(obj.poor_password())
      
        elif ask_complexity == 5:

            # Exit the loop

            print("Thanks For Using Password Generator App")
            print("x" * 40)
            break

        else:
            print("Invalid Choice")
            print("*" * 25)
    
    except ValueError:
        print("For Desired Ouput Enter Only Digits")
        print("*" * 25)

        








































# # Import Random 
# import random
# # Assign variables
# alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# digits = "123456789"
# special_characters = "!@#$%^&*()_+"

# # Take Input Password Length
# password_length = int(input("Enter password length: "))

# # Add Digits,Alphabets and Special Characters
# temp_password = alpha + digits + special_characters
# final_password = "".join(random.choice(temp_password) for i in range(password_length))

# print(final_password)

























# # Import Random 
# import random

# # Function for Password 
# def password(pass_length):
#     pass_length = int(pass_length)

#     # Assign variables 
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#     digits = "123456789"
#     special_characters = "!@#$%^&*()_+"
#     # Add Digits,Alphabets and Special Characters
#     password_generator = alpha + digits + special_characters

#     # Geberate Password
#     generate_password = "".join(random.choice(password_generator) for i in range(pass_length))
#     return generate_password

# # Take Input Password Length
# pass_length = int(input("Enter password length: "))

# # Calling Function
# print(password(pass_length))


















