"""
Models
"""
from django.db import models
from enumfields import Enum, EnumField


class Languages(Enum):
    """
    Defines congregation languages
    """
    English = 0
    Spanish = 1
    Portuguese = 2


class Weekdays(Enum):
    """
    Days of the week
    """
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class Congregation(models.Model):
    """
    This is the main model used to represent a congregeation.
    """
    guid = models.UUIDField(null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=20)
    language = EnumField(Languages)
    weekend_meeting_day = EnumField(Weekdays)
    meeting_time = models.TimeField()
    is_home_congregation = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.city}, {self.state}'
       