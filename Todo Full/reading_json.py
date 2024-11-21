import json

def read_students(file_name):
    students = {}
    with open(file_name, 'r') as file:
        reader = json.load(file)
        
    for student_id, student_info in reader.items():
        student = student_info[0]
        name =  student['name']
        grade = student['grade']
        group = student['group']
        
        students[student_id] = [name,grade,group]    
    return students
def display_content(info):
    if info:
        print(f'Name of the student: {info[0]}')
        print(f'Grade: {info[1]}')
        print(f'Group: {info[2]}') 
    else:
        print('student not found')

def main():
    file_name = r'C:\Users\Labinfo10\Documents\Quebec Martinez\archivos de chamba\data.json'

    student_info = read_students(file_name)
    number = input('Write the number of the Student: ')
    info = student_info.get(number)
    
    display_content(info)
    
main()