
from secret import get_secret_key
from menu import menu, create, find, find_accounts
# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

secret = get_secret_key()

passw = input('Please provide the master password to start using kallemanager3000: ')

def run(a, b):
    if a == b:
        print('You\'re in')
        choice = menu()
        while choice != 'Q':
            if choice == '1':
                create()
            if choice == '2':
                find_accounts()
            if choice == '3':
                find()
            else:
                choice = menu()

    else:
        print('no luck')
        restart = input('would you like to try again (y/n): ')
        if restart == 'y':
            run(a, b)
        else:
            quit()

run(passw, secret)
