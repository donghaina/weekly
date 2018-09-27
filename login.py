pw_list = ['#*#*', 'dhn123']
print(pw_list[-1])

def account_login():
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
        account_login()

account_login()