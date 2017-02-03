import pytest
import random
import datetime
import json

from cli_extrack import ExTrackCLI
import cli_extrack as cli

def random_user():
    random_key = "_{:04x}".format(random.randint(0, 16 ** 4))
    my_user = dict(cli.DEFAULT_ACCOUNT)
    my_user['username'] = my_user['username'] + random_key
    my_user['first_name'] = my_user['first_name'] + random_key
    my_user['password'] = 'test'
    return my_user


def random_record():
    token = "{:08}".format(random.randint(0, 16 ** 8))
    now = datetime.datetime.now()
    DEFAULT_RECORD = {
        'user_id': 0,
        'value': round(random.random() * 1000, 2),
        'date': now,
        'user_time': now.time(),
        'user_date': now.date(),
        'comment': 'THIS IS RANDOM COMMENT -- ' + token,
        'description': "FOOBAR -- " + token
    }
    return DEFAULT_RECORD


@pytest.fixture(scope='session', autouse=True)
def runserver():
    if True:
        return True
    else:
        from django.core.management import call_command
        from ..extrack.extrack import settings
        settings.configure()
        call_command(command_name='runserver')
        return ("http://localhost:8000")


@pytest.fixture(scope='session', autouse=False)
def admin_api():
    my = ExTrackCLI()
    my.get_auth(credentials={'username':'david','password':'test'})
    return my


@pytest.fixture(scope='function')
def usr_fixture(admin_api):
    decoder = json.JSONDecoder()
    new_user = random_user()
    res = admin_api.create_user( new_user )
    assert res.status_code == 201
    uid, = ( decoder.decode(res.text)[x] for x in ('id', ) )
    yield { 'id': uid, 'username': new_user['username'], 'password': new_user['password']}
    admin_api.delete_user( uid )

@pytest.fixture( scope='function')
def usr_api(usr_fixture):
    my = ExTrackCLI()
    new_usr = usr_fixture
    credentials = { 'username': new_usr['username'],
                    'password': new_usr['password']}
    res = my.get_auth( credentials=credentials )
    assert res is not None
    yield my
    del my