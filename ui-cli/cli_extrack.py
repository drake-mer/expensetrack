import requests
import configparser
import os

CONF_FILE=os.path.join(os.curdir,'cli_extrack.ini')

def default_user():
    return {
        "login": "david",
        "password": "password123",
        "port": "8000",
        "host": "localhost",
        "method": "http://"
    }

BASE_CONFIG = default_user()
BASE_URL = BASE_CONFIG['method'] + ':'.join([BASE_CONFIG[key] for key in ('host', 'port')])

def read_conf(conf_path=CONF_FILE):
    my = configparser.ConfigParser()
    my.read(conf_path)
    return (dict(my['USER']), dict(my['ADMIN']))

user, adm = read_conf()

def get_session( user=default_user() ):

    r = requests.get( user['method'] + user['host'] + ':' + user['port'] )
    return r

def create_user(name='John', login='foobar', password="*******"):
    CREATE_URL = "/".join([BASE_URL, 'user', 'create'])
    r = requests.get( CREATE_URL )
    return r



r = create_user()
print(r.content)