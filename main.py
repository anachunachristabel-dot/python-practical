name = input('What is your name?')
age = int(input('Type in your age'))
hobby = input('What is your favorite hobby?')
score = int(input('Give me your exam score'))
if score >=70:
    print("Excellent!")
elif score >=50:
    print("Good")
else :
    print("You need to improve")
print('My Name is', name ,',I am', age , 'years old. I love', hobby, 'and my exam score checker told me', score)