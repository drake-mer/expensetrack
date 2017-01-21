from django.test.utils import setup_test_environment
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

setup_test_environment()

from .models import Record, BookUser

class RouteUserTest(TestCase):
    """
    Simple testing of the routes defined into book/urls.py
    More complex testing could be placed here.
    """
    client=Client()

    def test_create_user(self):
        res = self.client.get( reverse( 'create_user' ) )
        print(res)
        self.assertNotEqual( res.status_code, 404)

    def test_get_user(self):
        res = self.client.get( reverse( 'get_all_users' ) )
        self.assertNotEqual( res.status_code, 404)
        print(res)

        res = self.client.get( reverse( 'get_user', args=[1] ) )
        self.assertNotEqual( res.status_code, 404)
        print(res)


    def test_update_user(self):
        res = self.client.get(reverse('update_user', args=[23]))
        self.assertNotEqual( res.status_code, 404 )


    def test_delete_user(self):
        res = self.client.get( reverse( 'delete_user', args=[32] ) )
        self.assertNotEqual( res.status_code, 404 )


class RouteRecordTest(TestCase):

    client=Client()
    def test_update_record(self):
        res = self.client.get( reverse('update_record', args=[43] ) )
        self.assertNotEqual( res.status_code, 404)

    def test_get_record(self):
        res = self.client.get( reverse( 'get_record', args=[52] ) )
        self.assertNotEqual( res.status_code, 404)
        res = self.client.get( reverse( 'get_all_records_of_user', args=[389] ) )
        self.assertNotEqual( res.status_code, 404)

    def test_delete_record(self):
        res = self.client.get( reverse( 'delete_record', args=[43] ) )
        self.assertNotEqual( res.status_code, 404)

    def test_get_weekly_record(self):
        res = self.client.get(reverse('get_weekly_record', args=[1,2039,20]) )
        self.assertNotEqual( res.status_code, 404)




# Create your tests here.
class BookTest(TestCase):
    NAME = "IDENTITIY_NAME"
    LOGIN = "IDENTITY_LOGIN"
    ADMIN_NAME = "ADMIN_NAME"
    ADMIN_LOGIN = "ADMIN_LOGIN"

    @classmethod
    def BookUserFixture(cls, name=NAME, login=LOGIN):
        return BookUser.objects.create_user( username=login,
                                             first_name=name,
                                             last_name='FAKE_LAST_NAME',
                                             password='*****' )



    def test_CreateBookUser(self):
        print(BookUser.objects.all())
        u=self.BookUserFixture()
        self.assertEqual( u.username, self.LOGIN )
        self.assertEqual( u.first_name, self.NAME)
        for my_obj in BookUser.objects.all():
            print(my_obj)

    def test_CreateRecord(self, val=345.2256):
        u=self.BookUserFixture()
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

    def test_ManyBookUsers(self, count=10):
        list_results=[]
        for x in range(count):
            ID = str(9999 + x)
            u = self.BookUserFixture( name="a_user" + ID, login="login" + ID )

        for a_user in BookUser.objects.filter( first_name__endswith="2"):
            print(a_user)

