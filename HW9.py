users = {}

def input_error(func):
    def wrapper(m, a):
        while Exception or not a == 'e':
            try:
                func(m)     
            except Exception: 
                print(f'{m}')
            else:
                break
    return wrapper

@input_error
def add(m):
    a = input()
    a = a.split(' ')
    users.update({a[0]: a[1]})

@input_error
def change(m):
    a = input()
    a = a.split(' ')
    users.update({a[0]: a[1]})

@input_error
def phone(m):
    a = input()
    print(users[a])



@input_error
def show_all(m):
    for key, value in users.items():
        print(key, value)   

@input_error
def help(m):
    return m

@input_error
def exit(m):
    return quit()   


commands = {'add':(add,'Enter user name and phone-number: ','Give me name and phone please'),
'good bye':(exit,'Good bye!',''),'close':(exit,'Good bye!',''),'exit':(exit,'Good bye!',''),
'hello':(help,'How can I help you?',''),'show all':(show_all,'Users list:',''),
'change':(change,'Enter user name and phone-number: ','Give me name and phone please'),
'phone':(phone,'Enter user name: ','Give me name'),}


def main():
    global users
    while True:
        input_string = input('Enter command: ' )
        input_string = input_string.lower()

        for el in commands:
            if input_string.find(el) != -1:
                print(commands[el][1])
                commands[el][0](commands[el][2])



if __name__ == '__main__':
    main()  
