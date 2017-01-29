import cli_extrack as cli
import random
from pprint import pprint
import json

dec = json.JSONDecoder()

test_to_run = []
test_to_run += ['create']
# test_to_run += [ 'delete' ]
# test_to_run += [ 'update' ]
# test_to_run += [ 'get_all' ]
# test_to_run += ['get']

if 'create' in test_to_run:
    for x in range(1):
        my_user = cli.DEFAULT_ACCOUNT
        my_user['username']=my_user['username']+"_{:04x}".format(random.randint(0, 16**4))
        my_user['first_name']+="_{:04x}".format(random.randint(0, 16**4))
        my_user['password'] = 'test'
        my = cli.create_user( user=my_user )
        assert my.status_code == 201


if 'get_all' in test_to_run:
    my = cli.get_all_users()
    status_code = my.status_code
    data = my.text
    data = dec.decode(data)  # type: dict
    pprint( data )

if 'get' in test_to_run:
    data = dec.decode(cli.get_all_users().text)
    for key, username in data.items():
        user_data = cli.get_usr(int(key)).text
        pprint(dec.decode(user_data))

if 'delete' in test_to_run:

    data = dec.decode(cli.get_all_users().text)
    list_of_keys_to_delete = [ int(x) for x in data if int(x)>10 ]
    print(list_of_keys_to_delete)

    for key in list_of_keys_to_delete:
        print("we are deleting this user:")
        pprint(data[str(key)])
        my = cli.delete_user( key )
        print(my.status_code)
