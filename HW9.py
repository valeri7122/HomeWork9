users = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)     
            except Exception: 
                print('Wrong enter. Repite please.')
    return wrapper

@input_error
def add():
    a = input()
    a = a.split(' ')
    return users.update({a[0]: a[1]})

@input_error
def change():
    a = input()
    a = a.split(' ')
    return users.update({a[0]: a[1]})

@input_error
def phone():
    a = input()
    print(users[a])

@input_error
def show_all():
    for key, value in users.items():
        print(key, value)   

@input_error
def hello():
    return 0

@input_error
def exit():
    return 'Good bye!'  

commands = {'add':(add,'Enter user name and phone-number: '),
'good bye':(exit,'Good bye!'),'close':(exit,'Good bye!'),'exit':(exit,'Good bye!'),
'hello':(hello,'How can I help you?'),'show all':(show_all,'Users list:'),
'change':(change,'Enter user name and phone-number: '),
'phone':(phone,'Enter user name: ')}

@input_error
def main():
    
    while True:
        input_string = input('Enter command: ').lower()
        print(commands[input_string][1])
        if commands[input_string][0]() == "Good bye!":
            break


if __name__ == '__main__':
    main() 
