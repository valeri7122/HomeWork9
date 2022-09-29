users = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        while Exception:
            try:
                func(*args, **kwargs)     
            except Exception: 
                print('Wrong enter. Repite please.')
            else:
                break
    return wrapper

@input_error
def add():
    a = input()
    a = a.split(' ')
    users.update({a[0]: a[1]})

@input_error
def change():
    a = input()
    a = a.split(' ')
    users.update({a[0]: a[1]})

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
    return quit()   

commands = {'add':(add,'Enter user name and phone-number: '),
'good bye':(exit,'Good bye!'),'close':(exit,'Good bye!'),'exit':(exit,'Good bye!'),
'hello':(hello,'How can I help you?'),'show all':(show_all,'Users list:'),
'change':(change,'Enter user name and phone-number: '),
'phone':(phone,'Enter user name: ')}

def main():
    while True:
        input_string = input('Enter command: ')
        input_string = input_string.lower()

        for el in commands:
            if input_string.find(el) != -1:
                print(commands[el][1])
                commands[el][0]()


if __name__ == '__main__':
    main()  
