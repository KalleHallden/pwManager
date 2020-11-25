import psycopg2


def store_passwords(password, user_email, username, url, app_name,user,pw,db_name):
    try:
        connection = psycopg2.connect(user=user, password=pw, host='127.0.0.1', database=db_name)
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_email, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def connect(user,pw,db_name):
    try:
        connection = psycopg2.connect(user=user, password=pw, host='127.0.0.1', database=db_name)
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_password(app_name,user,pw,db_name):
    try:
        connection = psycopg2.connect(user=user, password=pw, host='127.0.0.1', database=db_name)
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM accounts WHERE app_name = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        print('Password is: ' )
        #print(result)
        print(result[0])
    
    except (Exception, psycopg2.Error) as error:
        print(error)
def find_users(user_email,user,pw,db_name):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ') 
    try:
        connection = psycopg2.connect(user=user, password=pw, host='127.0.0.1', database=db_name)
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM accounts WHERE email = '""" + user_email + "'"
        cursor.execute(postgres_select_query, user_email)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row)-1):
                print(data[i] + row[i])
        print('')
        print('-'*30)
    except (Exception, psycopg2.Error) as error:
        print(error)
