from hash_maker import password
import subprocess 
from database_manager import store_passwords, find_users, find_password
from sys import platform

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

def create(a,b,c):
   print('Please proivide the name of the site or app you want to generate a password for')
   app_name = input()
   print('Please provide a simple password for this site: ')
   plaintext = input()
   passw = password(plaintext, app_name, 12)
   if platform == 'win32':
       subprocess.run('clip.exe', universal_newlines=True, input=passw,shell=True)
   elif platform == 'linux' or platform == 'linux2':
       subprocess.run('xclip', universal_newlines=True, input=passw,shell=True)
   else:
       print('Sorry, OS still not compatible')
       exit()
   print('-'*30)
   print('')
   print('Your password has now been created and copied to your clipboard')
   print('')
   print('-' *30)
   user_email = input('Please provide a user email for this app or site')
   username = input('Please provide a username for this app or site (if applicable)')
   if username == None:
       username = ''
   url = input('Please paste the url to the site that you are creating the password for')

# pylint: disable=too-many-function-args
   store_passwords(passw, user_email, username, url, app_name,a,b,c)

def find(a,b,c):
   print('Please provide the name of the site or app you want to find the password to')
   name = input()
   find_password(name,a,b,c)

def find_accounts(a,b,c):
   print('Please provide the email that you want to find accounts for')
   user_email = input() 
   find_users(user_email,a,b,c)
