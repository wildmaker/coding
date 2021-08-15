# 使用 get()

from dict4_1 import phone_book
def detail(people = phone_book()):
    print(people)
    labels = {
        'phone': 'phone number',
        'email': 'email'}
    name = input('Name:')
    request = input('Phone number (p) or email(e)?')
    key = request
    if request == 'p': key = 'phone'
    if request == 'e': key = 'email'
    person = people.get(name, {})
    print(person)
    label = labels.get(key, key)
    result = person.get(key, 'not available')
    print("%s's %s is %s" % (name, label, result))

# detail(people)