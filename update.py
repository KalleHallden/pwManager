from app import password_manager
from utils import config

def update(a,b,c,d,e,f):
    a = password_manager.launch.args[0]
    b = password_manager.launch.args[1]
    c = password_manager.launch.args[2]
    d = password_manager.launch.args[3]
    e = password_manager.launch.args[4]
    f = password_manager.launch.args[5]
    return a,b,c,d,e,f

new_config = update(*config.arg)
print(new_config)