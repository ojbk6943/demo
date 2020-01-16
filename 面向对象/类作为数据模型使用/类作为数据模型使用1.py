class Student(object):
    # 初始化中给对象属性赋值
    def __init__(self,name , age, phone):
        self.name = name
        self.age = age
        self.phone = phone

s1 = Student('张三', 22, 110)
print(s1)
# print(Student('张三', 22, 110).name)

s2 = Student('李四', 21, 120)
s3 = Student('王五', 21, 120)
# print(s1.name)
# student_list = [s1,s2,s3]
# print(student_list)
# s1 = student_list[0]
# # print()
# s1.name = '张三丰'
# print(s1.name)