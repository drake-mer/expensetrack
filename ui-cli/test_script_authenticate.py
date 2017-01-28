import cli_extrack as cli
import random
from pprint import pprint
import json
import datetime

dec = json.JSONDecoder()

DEFAULT_ACCOUNT = {
    'username': 'DEFAULT_USR_NAME',
    'first_name': 'DEFAULT_FIRST_NAME',
    'last_name': 'DEFAULT_LAST_NAME',
    'password': 'DEFAULT_PASSWD',
    'email': 'DEFAULT_MAIL@DOMAIN.COM'
}

my = cli.get_admin_auth()
print(my.text)