import datetime
name = str(input("请输入您的姓名："))
birth_day = int(input("请输入您的出生日期："))
age = datetime.date.today().year - birth_day
print(f"您好！{name}。您为{age}岁")
