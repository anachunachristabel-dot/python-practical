import os

def clear_screen():
    os.system('cls')
contacts = []
while True:
    clear_screen()
    print('1. Add contact')
    print('2. View contacts')
    print('3. Delete contacts')
    print('4. Count contacts')
    print('5. Exit')
    print('Your option must be a number')
    choice = int(input('Choose an option: '))
    if choice == 1:
        name = input('Enter a contact name: ')
        contacts.append(name)
    elif choice == 2:
        if len(contacts) == 0:
            print('There are no contacts to view')
        else:
            for number, name in enumerate(contacts, 1):
                print(number,'.', name)
    elif choice == 3:
        if len(contacts) == 0:
            print('There are no contacts to delete')
        else:
            for number, name in enumerate(contacts, 1):
                print(number,'.', name)
            name = input('Type the contact or number you want to delete: ')
            if name.isdigit():
                num = int(name)
                if 1 <= num <= len(contacts):
                    contacts.pop(num - 1)
                    print('Contact successfully deleted.')
                else:
                    print('Invalid contact number')
            elif name in contacts:
                contacts.remove(name)
                print('Contact successfully deleted.')
            else:
                print('Contact not found.')        
    elif choice ==4:
        print('You have', len(contacts), 'contacts.')
    elif choice == 5:
        print('Goodbye!')
        break
    else:
        print('Your choice is invalid!')
            