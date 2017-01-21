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
    CREATE_URL = "".join( x + "/" for x in [BASE_URL, 'user', 'create'] )
    r = requests.post(
        CREATE_URL,
        data=DEFAULT_ACCOUNT
    )
    return r

def delete_user( user_id ):
    DEL_USR_URL = "".join( x + "/" for x in [ BASE_URL, 'user', 'delete', str(user_id) ] )
    r = requests.delete( DEL_USR_URL )
    return r

def get_all_users():
    GET_ALL_USR_URL = "".join( x + "/" for x in [ BASE_URL, 'user', 'get' ] )
    r = requests.get(
        GET_ALL_USR_URL
    )
    return r

def get_usr(user_id):
    GET_REC_USR_URL = "/".join([BASE_URL, 'user', 'get', str(user_id)])
    return requests.get( GET_REC_USR_URL )

def get_records_of_usr(user_id):
    GET_REC_USR_URL = "/".join( [ BASE_URL, 'record', 'user', str(user_id) ] )

def update_record( record_id ):
    UP_REC_URL = "/".join( [ BASE_URL, 'record', "update", str(record_id) ] )

def get_record( record_id ):
    GET_REC_URL = "/".join( [ BASE_URL, 'record', str(record_id) ] )

def delete_record( record_id ):
    DEL_REC_URL = "/".join( [ BASE_URL, 'record', 'delete', str(record_id) ] )

