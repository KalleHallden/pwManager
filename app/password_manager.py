#importing configs and credentials
#import update -TODO fix circular import error
from utils import config
#from secret import get_secret_key
from menu import menu, create, find, find_accounts
#importing the crypto module
from cryptography.fernet import Fernet

#functions to generate\load an encryption key
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key','wb') as key_file:
        key_file.write(key)
def load_key():
    return open('secret.key','rb').read()

#functions to encrytpt and decrypt the password
def encrypt_pw(password):
    key = load_key()
    encoded_pw = password.encode()
    f = Fernet(key)
    encrypted_pw = f.encrypt(encoded_pw)
    return encrypted_pw
def decrypt_pw(enc_password):
    key = load_key()
    f = Fernet(key)
    decrypted_pw = f.decrypt(enc_password)
    return decrypted_pw

# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email


#this function is run to see whether the programm has already been run and parse data from the config_file.txt file
def launch(x):
    launch.launched = False
    if launch.launched == x:
        generate_key()
        print('Hello dear user! Please enter below the name you want to be called with.')
        launch.user_name = input('--> ')
        launch.password = encrypt_pw(input('Enter your password: '))
        launch.user = input('Enter the name of the user of your data base: ')
        launch.pw_db = encrypt_pw(input('The password of the data base: '))
        launch.dbname = input('Finally, the name of the data base: ')
        config.islaunched = True
        #arg = [launched+'\n',launch.user_name+'\n' , launch.password+'\n',launch.user+'\n',launch.pw_db+'\n',launch.dbname]
        #config_file = open('config_file.txt','w+')
        #config_file.writelines(arg)
        #config_file.close
        config.dbuser = launch.user
        config.dbname = launch.dbname
        config.dbpw = launch.pw_db
        config.user_name = launch.user_name
        config.password = launch.password
    else:
        launch.user_name = config.user_name
        launch.password = config.password
        launch.user = config.dbuser
        launch.pw_db = config.dbpw
        launch.dbname = config.dbname
    launch.args = [launch.launched,launch.user_name, launch.password,launch.user,launch.pw_db,launch.dbname]
    return launch.args

def run(n,p,a,b,c):
    passw = input(f'Please provide the master password to start using {n}: ')
    if passw == decrypt_pw(p):
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

launch(config.islaunched)
#debugging
#print(config.user_name,config.password)
run(launch.user_name, launch.password,launch.user,launch.pw_db,launch.dbname)

