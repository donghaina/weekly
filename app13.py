def account_login():
    pw = input('Password: ')
    if pw == 'dhn1001110123':
        print('Login success')
    else:
        print('Wrong password or invalid input')
        account_login()

account_login()