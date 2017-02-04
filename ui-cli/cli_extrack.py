import requests
import configparser
import json.decoder
import os

DEFAULT_ACCOUNT = {
    'username': 'DEFAULT_USR_NAME',
    'first_name': 'DEFAULT_FIRST_NAME',
    'last_name': 'DEFAULT_LAST_NAME',
    'password': 'DEFAULT_PASSWD',
    'email': 'DEFAULT_MAIL@DOMAIN.COM'
}

DEFAULT_SERVER = {
    "addr": "http://localhost:8080/",
    "auth_route": "api-token-auth",
    "user_route": "users",
    "record_route": "records"
}

CONF_FILE = os.path.join('cli_extrack.ini')

class ExTrackCLI:
    """ Class to interact with the API"""
    def __init__(self, token=None, serverconf=DEFAULT_SERVER):
        self.url = serverconf['addr']
        self.auth = serverconf['auth_route']
        self.users = serverconf['user_route']
        self.records = serverconf['record_route']
        self.token = token

    """ URL Routes """
    def generic_url(self, obj_name, obj_id):
        return self.url + self.__getattribute__(obj_name) + "/" + ((str(obj_id)+"/") if obj_id else "")

    def auth_url(self):
        return self.generic_url( 'auth', None)

    def record_url(self, record_id=None):
        return self.generic_url('records', record_id)

    def user_url(self, user_id=None):
        return self.generic_url('users', user_id)

    """ Authentication """
    def auth_header(self, token=None):
        the_token = self.token if self.token and token is None else token
        return { 'Authorization': "Token {}".format(the_token) }

    def get_auth( self, credentials=None ):
        r = requests.post( self.auth_url(), data= credentials )
        if r.status_code == 200:
            dec = json.decoder.JSONDecoder()
            try:
                self.token = dec.decode(r.text)['token']
            except:
                self.token = None
        return self.token

    """ CRUD Methods """
    def create_user( self, user=None ):
        return requests.post( self.user_url(), data=user, headers=self.auth_header())

    def update_user( self, user_id, user=None ):
        return requests.put( self.user_url(user_id), data=user, headers=self.auth_header() )

    def delete_user( self, user_id ):
        return requests.delete( self.user_url(user_id), headers=self.auth_header() )

    def get_all_users( self ):
        return requests.get( self.user_url(), headers=self.auth_header() )

    def get_usr(self, user_id):
        return requests.get( self.user_url(user_id), headers=self.auth_header() )

    def create_record(self, record=None):
        return requests.post( self.record_url(), data=record, headers=self.auth_header() )

    def update_record( self, record_id, record=None):
        return requests.put( self.record_url(record_id), data=record, headers=self.auth_header() )

    def delete_record( self, record_id ):
        return requests.delete( url=self.record_url(record_id), headers = self.auth_header() )

    def get_all_records(self):
        return requests.get( self.record_url(), headers=self.auth_header())

    def get_record( self, record_id ):
        return requests.get( self.record_url(record_id), headers=self.auth_header() )

    """Stalled conf reading method"""
    def read_conf(conf_path=CONF_FILE):
        my = configparser.ConfigParser()
        try:
            my.read(conf_path)
            return ()
        except:
            print("Warning: no conf file has been read")
