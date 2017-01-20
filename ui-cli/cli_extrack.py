import requests
import configparser
import os

CONF_FILE=os.path.join(os.curdir,'cli_extrack.ini')

def default_user():
    return {
        "login": "david",
        "password": "password123",
        "port": 8000,
        "host": "localhost",
        "method": "http"
    }

def read_conf(conf_path=CONF_FILE):
    my = configparser.ConfigParser()
    my.read(conf_path)
    return (dict(my['USER']), dict(my['ADMIN']))

user, adm = read_conf()

def connect_as( user=default_user() ):

    r = requests.get( user['host'] + ':' + user['port'],
                     auth=(user['login'], user['password']) )
    return r

