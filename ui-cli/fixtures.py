import pytest
import random

import cli_extrack as cli

def random_user():
    random_key = "_{:04x}".format(random.randint(0, 16 ** 4))
    my_user = dict(cli.DEFAULT_ACCOUNT)
    my_user['username'] = my_user['username'] + random_key
    my_user['first_name'] = my_user['first_name'] + random_key
    my_user['password'] = 'test'
    return my_user


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
    from cli_extrack import ExTrackCLI
    my = ExTrackCLI()
    my.get_auth(credentials={'username':'david','password':'test'})
    return my
