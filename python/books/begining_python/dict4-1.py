# 使用字典完成电话本增(删改)查

# 随机初始化一个电话本
import random, string

# 随机生成姓名
def rand_name():
    first_name = ["张", "曾", "李", "王", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "欧阳"]
    second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文",
                   "明浩", "光", "超", "军", "达"]
    name = random.choice(first_name) + random.choice(second_name)
    return name

# 随机生成手机号和邮箱
def rand_phone_email():
    phone_pre = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "185", "187", "188", "189"]
    phone = random.choice(phone_pre) + '%08d' % random.randint(0, 1e8-1)
    email = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,10))) + \
    ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,5))) + random.choice(['.com', '.cn'])
    d = dict(phone = phone,email = email)
    return d

# 初始化电话本
def directory(n=10):
    d = {}
    for i in range(1,n):
        name = rand_name()
        phone_email = rand_phone_email()
        d[name] = phone_email
        i+=1
    return d

people = directory()
print(people)
# 操作引导
q = ''
while q!='q':
    goal = input("What do you want to do? Press 'a' to add, Press 'f' to find, Press 'q' to quit.\n")
    if goal == 'a':
        name = input("Name:")
        phone = input("Phone:")
        email = input("Email:")
        people[name] = dict(phone = phone, email = email)
        print ("Add:" + name, people[name])
    elif goal == 'f':
        name = input("Name:")
        if name in people:
            print ("Found:" + name, people[name])
        else:
            print (name + " Not Found")
    elif goal =='q':
        q = goal
    else:
        pass

