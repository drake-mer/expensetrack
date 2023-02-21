from django.urls import re_path, include
from rest_framework.authtoken import views

from .views import \
    RecordDetailGeneric, \
    RecordListGeneric, \
    UserListGeneric, \
    UserDetailGeneric, \
    AuthTokenView

from .authentication import \
    Login, \
    Logout

urlpatterns = [
    # recorde management
    re_path(r'^records/$', RecordListGeneric.as_view(), name='record-list' ),
    re_path(r'^records/(?P<pk>[0-9]+)/$', RecordDetailGeneric.as_view(), name='record-detail'),
    # user management
    re_path(r'^users/$', UserListGeneric.as_view(), name='user-list' ),
    re_path(r'^users/(?P<pk>[0-9]+)/$', UserDetailGeneric.as_view(), name='user-detail' ),
    # identification
    re_path(r'^login/', Login.as_view(), name='login-view'),
    re_path(r'^logout/', Logout.as_view(), name='logout-view' ),
]

urlpatterns += [
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += [
    re_path(r'^api-token-auth/', AuthTokenView.as_view())
]
