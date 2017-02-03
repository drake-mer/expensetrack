import pytest
import json
import datetime

from fixtures import random_record, usr_api, usr_fixture, admin_api
N_TEST = 100
@pytest.mark.parametrize('number', [N_TEST])
def test_record_creation(number, usr_api):
    for x in range(number):
        my = usr_api.create_record( record=random_record())
        assert my.status_code == 201


@pytest.mark.parametrize('number', [N_TEST])
def test_record_create_update_get(number, usr_api):
    dec = json.JSONDecoder()
    test_string = "This String, standing for description, has been updated"
    records = []
    update_fields = ('comment', 'value', 'user_date', 'user_time', 'description')
    for x in range(number):
        my = usr_api.create_record( record=random_record())
        assert my.status_code == 201
        record_obj = dec.decode(my.text)
        record_obj['user_time'] = datetime.time()
        record_obj['description']=test_string
        records.append( record_obj  )

    for record in records:
        res = usr_api.update_record(record['id'], {field_name: record[field_name] for field_name in update_fields})
        assert res.status_code == 200

    for record in records:
        res = usr_api.get_record(record['id'])
        assert res.status_code == 200
        new_obj = dec.decode(res.text)
        assert new_obj['description'] == test_string



@pytest.mark.parametrize('number', [N_TEST])
def test_record_create_delete(number, usr_api):
    dec = json.JSONDecoder()
    records = []
    for x in range(number):
        my = usr_api.create_record( record=random_record())
        assert my.status_code == 201
        record_obj = dec.decode(my.text)
        records.append( record_obj  )

    for record in records:
        res = usr_api.delete_record(record['id'])
        assert res.status_code == 204
