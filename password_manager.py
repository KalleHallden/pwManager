
#from secret import get_secret_key
from menu import menu, create, find, find_accounts
# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email



#this function is run to see whether the programm has already been run and parse data from the config_file.txt file
def launch():
    config_file = open('config_file.txt','r')
    launched = False
    if launched == bool(int(config_file.readlines()[0])):
        config_file.close()
        print('Hello dear user! Please enter below the name you want to be called with.')
        launch.user_name = input('--> ')
        launch.password = input('Enter your password: ')
        launch.user = input('Enter the name of the user of your data base: ')
        launch.pw_db = input('The password of the data base: ')
        launch.dbname = input('Finally, the name of the data base: ')
        launched = '1'
        arg = [launched+'\n',launch.user_name+'\n' , launch.password+'\n',launch.user+'\n',launch.pw_db+'\n',launch.dbname]
        config_file = open('config_file.txt','w+')
        config_file.writelines(arg)
        config_file.close
    else:
        with open('config_file.txt') as f:
            data = f.read().splitlines()
        launch.user_name = data[1]
        launch.password = data[2]
        launch.user = data[3]
        launch.pw_db = data[4]
        launch.dbname = data[5]

    return launch.user_name, launch.password

def run(n,p,a,b,c):
    passw = input(f'Please provide the master password to start using {n}: ')
    if passw == p:
        print('You\'re in')

    else:
        print('no luck')
        exit() 

    choice = menu()
    while choice != 'Q':
        if choice == '1':
            create(a,b,c)
        if choice == '2':
            find_accounts(a,b,c)
        if choice == '3':
            find(a,b,c)
        else:
            choice = menu()
    exit()

launch()
run(launch.user_name, launch.password,launch.user,launch.pw_db,launch.dbname)
=======
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

