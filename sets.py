coding_club = {
    'Christabel',
    'Daniel',
    'Joy',
    'Michael'
}

chess_club = {
    'Joy',
    'Michael',
    'Sarah',
    'David'
}

def display_clubs():
    print('\n========== CODING CLUB ==========')
    for member in coding_club:
        print(member)

    print('\n========== CHESS CLUB ==========')
    for member in chess_club:
        print(member)

def show_common_members():
    print('\n========== Students in both clubs ==========')
    common_members = coding_club.intersection(chess_club)
    for members in common_members:
        print(members)

def show_only_coding_members():
    print('\n========== Students only in coding club ==========')
    coding_members = coding_club.difference(chess_club)
    for code_members in coding_members:
        print(code_members)

def show_only_chess_members():
    print('\n========== Students only in chess club ==========')
    chess_members = chess_club.difference(coding_club)
    for members in chess_members:
        print(members)

def show_unique_members():
    print('\n========== Students in only one club ==========')
    unique_members = coding_club.symmetric_difference(chess_club)
    for members in unique_members:
        print(members)

def add_member():
    club_question = input('Which club do you wish to add your student to? ').strip().lower()
    student_name =  input('What is the name of the student? ')
    if club_question == 'coding':
        coding_club.add(student_name)
        print('Student added successfully!')
        print('\n========== Students in coding club ==========')
        for new_member in coding_club:
            print(new_member)

    elif club_question == 'chess':
        chess_club.add(student_name)
        print('Student added successfully!')
        print('\n========== Students in chess club ==========')
        for new_member in chess_club:
            print(new_member)

    else:
        input('That club does not exist')

def remove_member():
    which_club = input('Which club is your student in? ').strip().lower()
    club_member = input("What is the student's name? ")
    if which_club == 'coding':
        coding_club.discard(club_member)
        print('Student removed successfully')
        print('\n========== Students in coding club ==========')
        for member in coding_club:
            print(member)
    elif which_club == 'chess':
        chess_club.discard(club_member)
        print('Student removed successfully')
        print('\n========== Students in chess club ==========')
        for member in chess_club:
            print(member)
    else:
        print('That club does not exist.')

def pause():
    print('Click enter to continue')
def menu():
    print('\n===== CLUB MEMBERSHIP CHECKER =====')

    print('\n1. Display Clubs')
    print('2. Show Common Members')
    print('3. Show Only Coding Members')
    print('4. Show Only Chess Members')
    print('5. Show Unique Members')
    print('6. Add Member')
    print('7. Remove Member')
    print('8. Exit')

    choice = input('Choose an option(1-8): ')

    if choice == '1':
        display_clubs()
        pause()
    elif choice == '2':
        show_common_members()
        pause()
    elif choice == '3':
        show_only_coding_members()
        pause()
    elif choice == '4':
        show_only_chess_members()
        pause()
    elif choice == '5':
        show_unique_members()
        pause()
    elif choice == '6':
        add_member()
        pause()
    elif choice == '7':
        remove_member()
        pause()
    elif choice == '8':
        print('Goodbye!')
    else:
        print('This option is invalid')

menu()