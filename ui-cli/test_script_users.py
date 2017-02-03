
import json
import pytest
from fixtures import admin_api, random_user

N_TEST = 100



@pytest.mark.parametrize('number', [N_TEST])
def test_create_get_delete( number, runserver, admin_api ):
    created_users = []
    decoder = json.JSONDecoder()

    # create test
    for x in range(number):
        my_user = random_user()
        my = admin_api.create_user( user=my_user )
        user_id = decoder.decode(my.text)['id']
        assert isinstance(user_id, (int,))
        created_users.append(user_id)
        assert my.status_code == 201

    ## get test
    for user_id in created_users:
        my = admin_api.get_usr(user_id)
        assert my.status_code == 200

    # delete test
    for user_id in created_users:
        my = admin_api.delete_user(user_id)
        assert my.status_code == 204


