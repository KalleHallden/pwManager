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
#credentials = [launched,user_name, password,user,pw_db,dbname]
#print(credentials)
#update(args,credentials)