from django.conf.urls import url, include
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
    url(r'^records/$', RecordListGeneric.as_view(), name='record-list' ),
    url(r'^records/(?P<pk>[0-9]+)/$', RecordDetailGeneric.as_view(), name='record-detail'),
    # user management
    url(r'^users/$', UserListGeneric.as_view(), name='user-list' ),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailGeneric.as_view(), name='user-detail' ),
    # identification
    url(r'^login/', Login.as_view(), name='login-view'),
    url(r'^logout/', Logout.as_view(), name='logout-view' ),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += [
    url(r'^api-token-auth/', AuthTokenView.as_view())
]