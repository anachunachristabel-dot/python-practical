students = {
    'student1': {
        'name': 'Christabel',
        'age': 14,
        'school': 'Silver Fountain College',
        'favorite_subject': 'Computer Science',
        'hobby': 'Coding'
    },

    'student2': {
        'name': 'Daniel',
        'age': 15,
        'school': 'Bright Future College',
        'favorite_subject': 'Designing',
        'hobby': 'Gaming'
    },
    'student3': {
        'name': 'Belle',
        'age': 16,
        'school': 'Ludi International College',
        'favorite_subject': 'Economics',
        'hobby': 'Tailoring'
    }
}
def display_students():
    for key, value in students.items():
        print(f"\n========== {key} ==========")
        for user_key, user_value in value.items():
            print(user_key, ':', user_value)

def view_one_student():
    user_input = input("Which Student's information do you want to view?").strip().lower()
    if user_input in students:
        selected_student = students[user_input]
        for view_key, view_value in selected_student.items():
            print(view_key, ':', view_value)
    else:
        print('That student does not exist')

def update_student():
    update_question = input('Which student do you want to update?: ').strip().lower()
    if update_question in students:
        selected_student = students[update_question]
        update_info = input('Which piece of information do you want to update?: ').strip().lower()
        if update_info in selected_student:
            new_update = input('What should the new value be?: ')
            selected_student[update_info] = new_update
            print('Student updated successfully!')
            for view_key, view_value in selected_student.items():
                print(view_key, ':', view_value)
        else:
            print('That piece of information does not exist')
    else:
        print('That student does not exist')

def add_new_student():
    new_student = input('Create a new student ID: ').strip().lower()
    if new_student in students:
        print('That student ID already exists')
    else:
        name = input("Type the student's name: ")
        age = int(input("enter the student's age: "))
        school = input('Enter the name of your school: ')
        favorite_subject = input('What is your favorite subject: ')
        hobby = input('Enter your favorite hobby: ')
        students[new_student] = {
            'name':  name,
            'age': age,
            'school': school,
            'favorite_subject': favorite_subject,
            'hobby': hobby 
        }
        print('Student added successfully!')
        for new_studentkey, new_studentvalue in students[new_student].items():
            print(new_studentkey, ':', new_studentvalue)

def delete_student():
    student_to_delete = input("Which student's id do you want to delete? ").strip().lower()
    if student_to_delete in students:
        students.pop(student_to_delete)
        print('Student ID successfully deleted!')
        display_students()
    else:
        print('That student does not exist')

def delete_key():
    deletion_choice = input("Which student's ID do you want to edit? ").strip().lower()
    if deletion_choice in students:
        selected_key = students[deletion_choice]
        key_to_delete = input('Which key do you want to delete? ')
        if key_to_delete in selected_key:
            selected_key.pop(key_to_delete)
            print('Key deleted successfully!')
            for key, value in selected_key.items():
                print(key, ':', value)
        else:
            print('That key does not exist.')
    else:
        print('That student does not exist.')

def pause():
    input("\nPress Enter to return to the menu...")

while True:
    print('\n========== STUDENT MANAGEMENT SYSTEM ==========')
    print('\n1. Display all students')
    print('2. View one student')
    print('3. Update student')
    print('4. Add new student')
    print('5. Delete student')
    print('6. Delete key')
    print('7. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        display_students()
        pause()
    elif choice == '2':
        view_one_student()
        pause()
    elif choice == '3':
        update_student()
        pause()
    elif choice == '4':
        add_new_student()
        pause()
    elif choice == '5':
        delete_student()
        pause()
    elif choice == '6':
        delete_key()
        pause()
    elif choice == '7':
        print('Goodbye!')
        break
    else:
        print("Invalid option. Please try again.")