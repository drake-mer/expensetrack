import cli_extrack as cli
import random
from pprint import pprint
import json

dec = json.JSONDecoder()

my_user = cli.DEFAULT_ACCOUNT
my_user['username']=my_user['username']+"_{:04x}".format(random.randint(0, 16**4))
my = cli.create_user( user=my_user )

my = cli.get_all_users()
status_code = my.status_code
data = my.text
data = dec.decode(data)  # type: dict
pprint( data )


for key, username in data.items():
    user_data = cli.get_usr(int(key)).text
    pprint(dec.decode(user_data))


list_of_keys_to_delete = [ int(x) for x in data if int(x)>10 ]
print(list_of_keys_to_delete)

for key in list_of_keys_to_delete:
    print("we are deleting this user:")
    pprint(data[str(key)])
    my = cli.delete_user( key )
    print(my.status_code)
