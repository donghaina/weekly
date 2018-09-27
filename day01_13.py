def account_login():
    password = input('Please enter password:')
    if password=='123456':
        print('Login success')
    else:
        print('Wrong password or invalid input')
        account_login()


account_login()