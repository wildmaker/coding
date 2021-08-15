# check username and PIN 

DATABASE = [
    ['albert', '1234'],
    ['alice', '4567'],
    ['smith','7894'],
    ['jones','8975']
]

def check(database = DATABASE):
    username = input("Username:")
    pin = input("PIN:")

    if [username,pin] in database:
        print("yes")
    else:
        print("no")

# 简陋的密码校验
def login(database = DATABASE):
    username=''
    pin=''
    logged= False
    while (not logged):
        while(not username):
            username = input("Username:")
        while(not pin):
            pin = input("pin:")
        if [username,pin] in database:
            print("yes")
            logged = True
        else:
            print("no")
            username=''
            pin=''