from django.db import models
from django.contrib.auth.models import User

class BookUser( User ):
    def __str__(self):
        fname = self.first_name
        lname = self.last_name
        login = self.username
        user_id = self.id
        return f"""User: id={user_id}
        name: {fname} {lname}
        login: {login}
        """

class Record( models.Model ):
    """
    An object that will contains an expense according to the project's specifications.

    An expense recording must have the following content (actually user provided) :

    - date
    - time
    - description
    - amount
    - comment

    An additionnal field will be the ID of the record (primary key) + A creation Date
    that will provide the default date and time for the record.

    """
    user_id = models.ForeignKey( BookUser )
    record_date = models.DateTimeField( auto_now=True, auto_created=True )
    user_date = models.DateField()
    user_time = models.TimeField()
    value = models.DecimalField( decimal_places=2, max_digits=15 )
    description = models.CharField( max_length=50 )
    comment = models.CharField( max_length=200 )

    def __str__(self):
        the_id = self.id
        creation_date = self.record_date
        amount = self.value
        desc = self.description
        com = self.comment
        return f"""Record {the_id}:
        date: {creation_date}
        amount: {amount}
        desc: {desc}
        comment: {com}
        """


    
