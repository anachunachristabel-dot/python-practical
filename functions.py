import os

def career_profile(name, career, *skills, **details):
    print(f'My name is {name}.')
    print(f'I want to become a {career}.')

    print('My skills are: ')
    for skill in skills:
        print('-', skill)

    print('Other details: ')
    for key, value in details.items():
        print(f'{key}: {value}')

name = input('Enter your name: ')
career = input('Enter your career: ')
skills = []
while True:
    skill = input('Enter a skill or type "done" to finish: ')

    if skill.strip().lower() == 'done':
        break
    skills.append(skill)
school = input('Enter your school: ')
certi = input('Enter your school leaving certificate details: ')

os.system('cls' if os.name == 'nt' else 'clear')

career_profile(name, career, *skills, school=school, certi=certi)