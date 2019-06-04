# 判断年满18
age = int(input("输入年龄: "))

if 0 <= age <= 120:
    print("输入正确")
    if not age < int(18):
        print("年满18")
    else:
        print("未成年")
else:
    print("输入错误")

print("判断完毕")

if age < 18:
    print("未成年")
elif (age >= 18 and age < 30):
    print("青年")
elif (age >= 30 and age < 50):
    print("中年")
else:
    print("老年")

# 判断成绩
score = 60
score1 = 69
score2 = 74
score3 = 46

if ((score1 > score) or (score2 > score) or (score3 > score)):
    print("pass exam")
    age = 90
else:
    print("can't pass exam")

