import requests
import configparser
import os

CONF_FILE=os.path.join(os.curdir,'cli_extrack.ini')

DEFAULT_ACCOUNT = {
    'username': 'DEFAULT_USR_NAME',
    'first_name': 'DEFAULT_FIRST_NAME',
    'last_name': 'DEFAULT_LAST_NAME',
    'password': 'DEFAULT_PASSWD',
    'email': 'DEFAULT_MAIL@DOMAIN.COM'
}



DEFAULT_USER = {
    "login": DEFAULT_ACCOUNT['username'],
    "password": DEFAULT_ACCOUNT['password']
}

DEFAULT_SERVER = {
    "port": "8000",
    "host": "localhost",
    "method": "http://"
}

conf = DEFAULT_SERVER
BASE_URL = conf['method'] + ':'.join( [conf[key] for key in ('host', 'port')])

def read_conf(conf_path=CONF_FILE):
    my = configparser.ConfigParser()
    my.read(conf_path)
    return (dict(my['USER']), dict(my['ADMIN']))

user, adm = read_conf()

def get_session( user=DEFAULT_USER ):
    LOG_URL = "".join( x+"/" for x in [BASE_URL, 'login'] )
    r = requests.post(
        LOG_URL,
        data={ 'login': user['login'], 'password': user['password'] }
    )
    return r

def create_user( user=DEFAULT_USER ):
    CREATE_URL = "".join( x + "/" for x in [BASE_URL, 'users'] )
    r = requests.post(
        CREATE_URL,
        data=user,
        headers = { 'Authorization': "Token b4a8a313eb062dbff8c7b9cfee28e9bcfddb9dc8"}
    )
    return r

def delete_user( user_id ):
    DEL_USR_URL = "".join( x + "/" for x in [ BASE_URL, 'users', str(user_id) ] )
    r = requests.delete( DEL_USR_URL )
    return r

def get_all_users():
    GET_ALL_USR_URL = "".join( x + "/" for x in [ BASE_URL, 'users' ] )
    r = requests.get(
        GET_ALL_USR_URL
    )
    return r

def get_usr(user_id):
    GET_REC_USR_URL = "".join([ x + "/" for x in [BASE_URL, 'users', str(user_id)] ])
    return requests.get( GET_REC_USR_URL )

def create_record(user_id, record={}):
    GET_REC_USR_URL = "".join( [ x+"/" for x in [BASE_URL, 'record', 'user', str(user_id), 'add' ] ] )
    return requests.post( GET_REC_USR_URL, data=record)

def get_records_of_usr(user_id):
    GET_REC_USR_URL = "".join( [x+"/" for x in [ BASE_URL, 'records', 'user', str(user_id) ]] )
    return requests.get( GET_REC_USR_URL )

def update_record( record_id, record={}):
    UP_REC_URL = "".join( [ x + "/" for x in [ BASE_URL, 'record', str(record_id) ] ] )
    return requests.post( UP_REC_URL, data=record )

def get_record( record_id ):
    GET_REC_URL = "".join( [x + "/" for x in [ BASE_URL, 'record', str(record_id) ] ])
    return requests.get( GET_REC_URL )

def delete_record( record_id ):
    DEL_REC_URL = "".join( [ x+"/" for x in [BASE_URL, 'record', str(record_id) ] ])
    return requests.delete( DEL_REC_URL )

def get_auth_token(data=None):
    AUTH_URL = "".join( [x+"/" for x in [BASE_URL, 'api-token-auth']])
    return requests.post(AUTH_URL, data=data)

def get_admin_auth(name='david', password='test'):
    result = get_auth_token( data={'username': name, 'password': password} )
    return result