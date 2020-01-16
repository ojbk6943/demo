g = float(input("请输入您的成绩："))
if 100>=g>=90:
    if 100>=g>=95:
        print("奖励笔记本一台")
    else:
        print("奖励一个棒棒糖")
elif g>=80:
    print("优秀")
elif g>=60:
    print("及格")
else:
    print("不及格")
