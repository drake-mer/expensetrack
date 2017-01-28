from django.conf.urls import url, include

from .views import \
    RecordDetailGeneric, \
    RecordListGeneric, \
    UserListGeneric, \
    UserDetailGeneric

urlpatterns = [
    url(r'^records/$', RecordListGeneric.as_view(), name='record-list' ),
    url(r'^records/(?P<pk>[0-9]+)/$', RecordDetailGeneric.as_view(), name='record-detail'),

    url(r'^users/$', UserListGeneric.as_view(), name='user-list' ),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailGeneric.as_view(), name='user-detail' )
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]