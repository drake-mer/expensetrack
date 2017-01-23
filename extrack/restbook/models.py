from django.db import models

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
    owner = models.ForeignKey('auth.User', related_name='records', on_delete=models.CASCADE)
    record_date = models.DateTimeField( auto_now=True, auto_created=True )
    user_date = models.DateField()
    user_time = models.TimeField()
    value = models.DecimalField( decimal_places=2, max_digits=15 )
    description = models.CharField( max_length=50 )
    comment = models.CharField( max_length=200 )

    class Meta:
        ordering = ('id',)
