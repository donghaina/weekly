pw_list = ['#*#*', 'dhn123']

def account_login():
    tries = 3
    while tries > 0:
        pw = input('Password:')
        pw_correct = pw == pw_list[-1]
        pw_reset = pw == pw_list[0]
        if pw_correct:
            print('Login success!')
        elif pw_reset:
            new_pw = input('Enter a new password:')
            pw_list.append(new_pw)
            print('Your password has changed successfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            tries = tries -1
            print(tries, 'times left')
    else:
        print('Your account has been suspended')
account_login()