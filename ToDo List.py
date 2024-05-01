
# Define a class named ToDoList

class ToDoList:
    task = []       # Class variable to store tasks

    def __init__(self):

        # Constructor method to initialize the ToDoList object.

        print("Welcome to Todo List App")
        print("*" * 25)

    def View_Task(self):

        # Method to display tasks.

        if self.task:
            print("Your Tasks:")
            print("*" * 30)
            for i in range(len(self.task)):
                print(f"{i+1}. {self.task[i]}")
                print("*" * 30)

        else:
            print("No Tasks!")

    def Add_Task(self):

        # Method to add a new task.

        while True:
        
            self.add_task = input("Enter Your Task: ")
            print("*" * 30)

            if self.add_task == "":
                print("Invalid Task")
                print("*" * 30)
            
            else:
                print("Task Added Successfully")
                self.task.append(self.add_task)
                break

    def Update_Task(self):

        # Method to update an existing task.

        if self.task:
            self.View_Task()
            while True:
                self.ask_task_number = (input("Enter the Task Number to Update:: "))
                print("*" * 30)

                if self.ask_task_number == "":
                    print("Invalid Task Number")
                    print("*" * 30)

                elif "1" <= self.ask_task_number <= str(len(self.task)):
                    while True:

                        self.update_task = input("Enter your updated Task: ")
                        print("*" * 30)

                        if self.update_task == "":
                            print("Invalid Task")
                            print("*" * 30)

                        else:
                            # Updating the task

                            self.task[int(self.ask_task_number) -1] = self.update_task
                            print("Task Updated Successfully!")
                            print("*" * 30)
                            break
                    break
            
                else:
                    print("Invalid Task Number! Please enter a valid task number.")

        else:
            print("No Tasks")


    def Delete_Task(self):

        # Method to delete a task.

        if self.task:
            self.View_Task()
            while True:

                self.del_task_Number = (input("Enter the Task Number to Delete: "))
                if self.del_task_Number == "":
                    print("Invalid Choice")
                    print("*" * 30)

                elif "1"<= self.del_task_Number <= str(len(self.task)):

                    # Deleting the task

                    del self.task[int(self.del_task_Number) -1]
                    print("Task Delete Successfully")
                    print("*" * 30)
                    break

                else:
                    print("Invalid Task Number! Please enter a valid task number.")
                    print("*" * 30)

        else:
            print("No Tasks")

# Creating an instance of ToDoList

obj = ToDoList()

# Main menu options

print("1: View Tasks\n2: Add Tasks\n3: Update Task\n4: Delete Task\n5: Exit")
print("*" * 30)


while True:
    choice = int(input("Enter Your Choice: "))
    print("*" * 25)
    if choice == 1:
        obj.View_Task()

    elif choice == 2:
        obj.Add_Task()

    elif choice == 3:
        obj.Update_Task()
    
    elif choice == 4:
        obj.Delete_Task()

    elif choice == 5:
        print("Thanks For Using My ToDo List App!")
        print("x" * 40)
        break

    else:
        print("Invalid Choice! Please Enter a Number between 1 and 5.")
        print("*" * 30)

































          












