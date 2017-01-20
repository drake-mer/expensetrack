from django.test import TestCase
from django.utils import timezone

import random

from .models import Record, User

# Create your tests here.
class BookTest(TestCase):
    NAME = "WHAT'S MY MOTHER FUCKING NAME ?"
    LOGIN = "I'M LOGGIN IN YOUR ASS"
    ADMIN_NAME = "ADMIN_NAME"
    ADMIN_LOGIN = "ADMIN_LOGIN"

    @classmethod
    def UserFixture(cls, name=NAME, login=LOGIN):
        u = User(user_name=name,
                 user_login=login,
                 user_type=1)
        u.save()
        return u


    @classmethod
    def AdminFixture(cls):
        u = User(user_name=cls.ADMIN_NAME,
                 user_login=cls.ADMIN_LOGIN,
                 user_type=2)
        u.save()
        return u


    def test_CreateUser(self):
        print(User.objects.all())
        u=self.UserFixture()
        self.assertEqual( u.user_login, self.LOGIN )
        self.assertEqual( u.user_name, self.NAME)
        for my_obj in User.objects.all():
            print(my_obj)

    def test_CreateRecord(self, val=345.2256):
        u=self.UserFixture()
        v=self.UserFixture()
        r = Record(
            user_id = u,
            description = "buying a pair of Shoes",
            comment = "this one was really expensive",
            value = val,
            user_date = timezone.now().date(),
            user_time = timezone.now().time()
        )
        r.save()

        for r in Record.objects.all():
            self.assertAlmostEqual( float(r.value), val, places=2 )
            print(r)

    def test_ManyUsers(self, count=100):
        list_results=[]
        for x in range(count):
            ID = str(random.randint(1000,9999))
            u = self.UserFixture( name="user" + ID, login="login" + ID )
            u.save()

        for user in User.objects.filter( user_name__endswith="9"):
            print(user)

