users = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)     
        except KeyError:
            print('Enter user name:')
        except ValueError:
            print('Enter correct type:')
        except IndexError:
            print('Give me name and phone please:')
    return wrapper


@input_error
def add(func_arg):
    a = func_arg.split(' ')
    return users.update({a[0]: a[1]})

@input_error
def change(func_arg):
    a = func_arg.split(' ')
    return users.update({a[0]: a[1]})

@input_error
def phone(func_arg):
    p = users[func_arg]
    print(p)

@input_error
def show_all():
    print('Users list:')
    for key, value in users.items():
        print(f'{key}:{value}')  

@input_error
def hello():
    return 'How can I help you?'
    
@input_error
def exit():
    return 'Good bye!'  

commands = {
'add':add,
'good bye':exit,
'close':exit,
'exit':exit,
'hello':hello,
'show all':show_all,
'change':change,
'phone':phone}


def main():
    while True:
        input_string = input('Enter command: ').strip().lower()
        if input_string == 'add' or input_string == 'change':
            commands[input_string](input('Enter user name and phone-number: ').strip().lower())
        elif input_string == "phone":
            commands[input_string](input('Enter user name: ').strip().lower())
        elif input_string == "hello":
            print(commands[input_string]())
        elif commands[input_string]() == "Good bye!":
            print(commands[input_string]())
            break    


if __name__ == '__main__':
    main() 
