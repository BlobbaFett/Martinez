# A simple to-do list manager for high school students using functions and list comprehension

# Initial to-do list
todo_list = ["Math homework", "Science project", "Read history book", "Practice piano"]

# Function to display the current to-do list
def display_todo_list():
    for list in todo_list:
        print(list)

# Function to add a new task
def add_task():
    task = input('Write the new task: ')
    todo_list.append(task)    

# Function to remove a task by its name
def remove_task(): 
    task = input('Write the task you want to delete: ')
    if task in todo_list:
        todo_list.remove(task)

# Function to find the index of a task
def find_task():
    task = input('Task you want to know: ')
    print(f'{task} is in position {todo_list.index(task)+1} of the list')

# Function to complete and remove the first task
def complete_task():
        print(f"{todo_list.pop(0)} was completed")

# Function to filter tasks containing a specific keyword using list comprehension
def filter_tasks():
    keyword = input('Input a keyword to find the task: ')
    filtered_tasks = [task for task in todo_list if keyword in task]
    print(f"\nTasks containing '{keyword}':")
    print(filtered_tasks if filtered_tasks else "No tasks found.")

# Main program

# Main menu to choose options
def main():
    while True:
        print("\nTo-Do List Manager Menu")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Find Task")
        print("5. Complete First Task")
        print("6. Filter Tasks by Keyword")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")

        #TODO create the if staments for the user. 
        if choice == '1':
            display_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            find_task()
        elif choice == '5':
            complete_task()
        elif choice == '6':
            filter_tasks()
        elif choice == '7':
            break
        else:
            print('Invalid option')

# Run the main function
main()

