from django.conf.urls import url

from .views import users, ops, perms

urlpatterns = [

    url(r'^users/$', users.get_users, name='get_all_users'),
    url(r'^user/create/$', users.create_user, name='create_user'),
    url(r'^user/get/(?P<user_id>[0-9]+)/$', users.get_user_from_id, name='get_user'),
    url(r'^user/delete/(?P<user_id>[0-9]+)/$', users.delete_user_from_id, name='delete_user'),
    url(r'^user/update/(?P<user_id>[0-9]+)/$', users.update_user, name='update_user'),


    url(r'^records/user/(?P<user_id>[0-9]+)/$', ops.get_records, name='get_all_records_of_user'),
    url(r'^record/(?P<record_id>[0-9]+)/$', ops.get_record_from_id, name='get_record'),
    url(r'^record/user/(?P<user_id>[0-9]+)/add/$', ops.add_record, name='add_record'),
    url(r'^record/delete/(?P<record_id>[0-9]+)/$', ops.delete_record, name='delete_record'),
    url(r'^record/update/(?P<record_id>[0-9]+)/$', ops.update_record_from_id, name='update_record'),
    url(r'^record/user/(?P<user_id>[0-9]+)/y/(?P<year>[0-9]{4})/w/(?P<week>[0-9]{1,2})/',
        ops.get_records_by_user_by_week, name='get_weekly_record'),

    url(r'^login/$', perms.get_session, name='get_session' )
]
