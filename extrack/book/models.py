from django.db import models

USER_KINDS = (
    (1,'Single User'),
    (2,'Admin')
)

class User( models.Model ):

    user_type = models.IntegerField( choices=USER_KINDS )
    user_name = models.CharField( max_length=20, default="" )
    user_login = models.CharField( max_length=20, default="" )

    def __str__(self):
        name = self.user_name
        login = self.user_login
        type = self.user_type
        user_id = self.id
        return f"""User: id={user_id}
        name: {name}
        login: {login}
        type: {type}
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
    user_id = models.ForeignKey( User )
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


    
