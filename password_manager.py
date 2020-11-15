
from secret import get_secret_key
from menu import menu, create, find, find_accounts
# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

secret = get_secret_key()

passw = input('Please provide the master password to start using kallemanager3000: ')

if passw == secret:
    print('You\'re in')

else:
    print('no luck')
    exit() 

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
exit()
