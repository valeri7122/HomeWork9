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
    users[func_arg[0]] = func_arg[1]
    return 'A new contact has been added'

@input_error
def change(func_arg):
    users[func_arg[0]] = func_arg[1]
    return 'The contact has been changed'

@input_error
def phone(func_arg):
    return users[func_arg[0]]

@input_error
def show_all(_=None):
    print('Users list:')
    return users 

@input_error
def hello(_=None):
    return 'How can I help you?'
    
@input_error
def exit(_=None):
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

        print('Enter command:')
        
        input_string = input().lower()


        if input_string.split()[0] in commands and len(input_string.split()) > 1:

            print(commands[input_string.split()[0]](input_string.split()[1:]))
            
        elif input_string in commands:
            
            print(commands[input_string](input_string))
            
            if commands[input_string](input_string) == "Good bye!":
                break


 
if __name__ == '__main__':
    main() 
