age = int(input('How old are you?'))
schid = input('Do you have a school ID?')
student = input('Are you a student?')
if age >=13 and schid == 'yes' or student == 'yes' and schid == 'yes':
    print('You can enter')
else:
    print('You cannot enter')