from django.conf.urls import url

from .views import users
from .views import ops

urlpatterns = [
    url(r'^u/$', users.get_all_users, name='index'),
]
