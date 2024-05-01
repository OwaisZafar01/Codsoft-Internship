# Import the random module

import random

# Define a class named RockPaperScissor

class RockPaperScissor:
    User_record = 0
    Computer_record = 0
    tie_record = 0

    # When an object is created, this constructor is called
    def __init__(self):
        print("Welcome to Rock,Paper,Scissor Game")
        print("*" * 40)

    # Function to Get Input from User

    def user_input(self):
        while True:
            try:
                # Valid options are: rock, paper, scissor. Please choose one.

                self.choice_input = input("Enter rock,paper,scissor: ")
                print("*" * 35)
                self.choice_input = self.choice_input.lower()

                if (self.choice_input == "rock") or (self.choice_input == "paper") or (self.choice_input == "scissor"):
                    break

                else:
                    print("Enter valid option")
                    print("*" * 25)
                    continue

            except ValueError:
                print("For Desired Output Enter given options only")
                print("*" * 35)

    # Function to Generate Computer's Turn

    def computer_play(self):

        self.computer_options = ["rock","paper","scissor"]
        self.computer_turn = random.choice(self.computer_options)

        return f"Computer Turn: {self.computer_turn}"

    # Function to Determine the Winner

    def check_winner(self):
        if self.choice_input == self.computer_turn:
            print("Tie")
            self.tie_record += 1

        elif (self.choice_input == "rock" and self.computer_turn == "scissor") or \
        (self.choice_input == "paper" and self.computer_turn == "rock") or \
        (self.choice_input == "scissor" and self.computer_turn == "paper"):
            
            print("User Wins")

            # Increase User's Score
            self.User_record += 1

        else:
            print("Computer Wins")

            # Increase Computer's Score

            self.Computer_record +=1

    # Function to Update Game Winner or Tie Records

    def Game_records(self):
        return f"User Wins {self.User_record} times.\nComputer Wins {self.Computer_record} times\nTied {self.tie_record} times"
    

# Create an instance of the RockPaperScissor class

obj = RockPaperScissor()

# Prompt the user to select an option:

print("1: Play Game\n2: Check Records\n3: Exit")
print("*" * 30)

while True:
    try:
       # Only accept digits (1, 2, 3) as input

        ask_choice = int(input("Enter your Choice: "))
        print("*" * 25)

        if ask_choice == 1:
            
            # Prompt the user to enter their choice: rock, paper, or scissor

            obj.user_input()

           # Generate the computer's turn

            print(obj.computer_play())

            # Determine the winner of the game

            obj.check_winner()

        elif ask_choice == 2:

            # Record For game Players

            print(obj.Game_records())

        elif ask_choice == 3:

            # Exiting the game loop

            print("Thanks For Playing the Game")
            print("x" * 35)
            break

        else:
            print("Invalid Choice")
            print("*" * 25)

    except ValueError:
        print("For Desired Ouput Enter Digits Only")
        print("*" * 35)













