from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField 

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(max_length=15, blank=True, null=True)

    POLISH = 'PL'
    ENGLISH = 'EN'
    MATH = 'MA'
    CHEMISTRY = 'CH'
    PHYSICS = 'PH'
    HISTORY = 'HI'
    GEOGRAPHY = 'GE'

    SUBJECT_CHOICES = [
        (POLISH, 'J. Polski'),
        (ENGLISH, 'J. Angielski'),
        (MATH, 'Matematyka'),
        (CHEMISTRY, 'Chemia'),
        (PHYSICS, 'Fizyka'),
        (HISTORY, 'Historia'),
        (GEOGRAPHY, 'Geografia'),
    ]

    subjects = MultiSelectField(choices=SUBJECT_CHOICES, blank=True, null=True)

    PRIMARY_SCHOOL = 'PS'
    HIGH_SCHOOL = 'HS'
    TECHNICAL_SCHOOL = 'TS'
    VOCATIONAL_SCHOOL = 'VS'

    SCHOOL_TYPE_CHOICES = [
        (HIGH_SCHOOL, 'Szkoła średnia liceum'),
        (TECHNICAL_SCHOOL, 'Szkoła średnia technikum'),
    ]

    school_type = models.CharField(
        max_length=2,
        choices=SCHOOL_TYPE_CHOICES,
        blank=True,
        null=True
    )

    class GradeChoices(models.IntegerChoices):
        PS1 = 1, '1'
        PS2 = 2, '2'
        PS3 = 3, '3'
        PS4 = 4, '4'
        PS5 = 5, '5'

    grade = models.PositiveSmallIntegerField(
        choices=GradeChoices.choices,
        blank=True,
        null=True
    )

    email_confirmed = models.BooleanField(default=False)
    phone_confirmed = models.BooleanField(default=False)

    def get_subjects_display(self):
        subject_dict = dict(self.SUBJECT_CHOICES)
        return ', '.join([subject_dict.get(subject, subject) for subject in self.subjects])
