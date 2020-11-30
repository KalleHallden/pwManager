from cryptography.fernet import Fernet

#from password_manager import launched,user_name, password,user,pw_db,dbname
#import password_manager
#args = ["islaunched","user_name","password","dbuser","dbname","dbpw"]

def update(arg,arg2):
    f = open('utils/config.py','w+')
    for i in range(len(arg)):
        if i == 0:
            f.write(f"{arg[0]} = True\n")
        else:
            if type(arg2[i]) == bytes:
                f.write(f"""{arg[i]} = {arg2[i]}\n""")
            else:
                f.write(f"""{arg[i]} = '{arg2[i]}'\n""")
            if i == 6:
                break
    f.close

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
    decoded_pw = decrypted_pw.decode()
    return decoded_pw
#credentials = [launched,user_name, password,user,pw_db,dbname]
#print(credentials)
#update(args,credentials)