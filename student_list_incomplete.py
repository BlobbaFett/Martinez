# Initial list of students
student = ["Emily Johnson","Michael Smith","Sarah Brown","David Lee","Jessica Garcia","Daniel Martinez","Olivia Davis","Christopher Wilson","Ava Taylor","James Anderson"]


def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    for names in student:
        print(names)
    print(f"_____________________________________") 

# Add a new student to the list
def add_student():
    student.append(input('Add a new student: '))
    display_students()

# Remove a student from the list by name
def remove_student():
    name = input('Write the name of the student to delete it: ')
    if name in student:
        student.remove(name)
    if name in student:
        print(f"{name} exist in the list.")
    else:
        print(f"{name} doesn't exist in the list.")
    display_students()

# remove a student from the end of the list
def pop_student():
    last = student.pop()
    print(f'{last} was removed from the list' )
    if not student:
        print('There is not more students left')
    display_students()

# Update a student's name in the list
def update_student():
    name = input('Name of the Student: ')
    new = input('Write the name of the student to update: ')
    find = student.index(name)
    student[find] = new
    if not new:
        print('This name do not exits')
    else:
        print('This name exist')
    display_students()

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            pop_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            break        
        else:
            print('Invalid choice')
        
# Start the program
menu()
