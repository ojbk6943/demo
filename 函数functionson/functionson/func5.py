def statmf(students, minage):
    #将局部变量改为全局变量
    global malelist
    malelist = []
    global female
    female = []
    for student in students:
        if student['age'] > minage:
            if student['gender'] == 'male':
                malelist.append(student['name'])
            elif student['gender'] == 'female':
                female.append(student['name'])

#存放个人信息，列表中每个元素是字典，
students = [
    {'age': 18, 'name': 'augus1', 'gender': 'male'},
    {'age': 20, 'name': 'augus2', 'gender': 'male'},
    {'age': 46, 'name': 'augus3', 'gender': 'male'},
    {'age': 12, 'name': 'augus4', 'gender': 'male'},
    {'age': 23, 'name': 'augus5', 'gender': 'female'},
    {'age': 30, 'name': 'augus6', 'gender': 'female'},
    {'age': 40, 'name': 'augus7', 'gender': 'male'},
]

statmf(students, 15)
print('the male   students are %s' % '='.join(malelist))
print('the female students are %s' % ''.join(female))