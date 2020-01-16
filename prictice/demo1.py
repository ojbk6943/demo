students = [
    {'age': 18, 'name': 'augus1', 'gender': 'male'},
    {'age': 20, 'name': 'augus2', 'gender': 'male'},
    {'age': 46, 'name': 'augus3', 'gender': 'male'},
    {'age': 12, 'name': 'augus4', 'gender': 'male'},
    {'age': 23, 'name': 'augus5', 'gender': 'female'},
    {'age': 30, 'name': 'augus6', 'gender': 'female'},
    {'age': 40, 'name': 'augus7', 'gender': 'male'},
]

def statmf(students, minage):
    global Mname,Fname
    Mname = []
    Fname = []
    for one in students:
        if one["age"] > minage:
            if one["gender"] == "male":
                Mname.append(one["name"])
            elif one["gender"] == "female":
                Fname.append(one["name"])

statmf(students,18)

print('年龄复合要求的男性有哪些 %s' % '&&&'.join(Mname))




