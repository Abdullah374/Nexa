from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# class Course(models.Model):
#     course_name = models.CharField(max_length=100)  # Full name of the course
#     abbreviation = models.CharField(max_length=10)  # Abbreviation like 'B.Tech', 'MBA', etc.

#     def __str__(self):
#         return self.course_name

# # Define the College model
# class College(models.Model):
#     name = models.CharField(max_length=255)  # Name of the college
#     city = models.CharField(max_length=100)  # City where the college is located
#     state = models.CharField(max_length=100)  # State where the college is located
#     nirfRank = models.IntegerField(null=True)  # NIRF ranking of the college
#     course_name = models.ManyToManyField(Course, related_name='colleges')  # Many-to-many relationship with Course

#     def __str__(self):
#         return self.name

class College(models.Model):
    application_number = models.CharField(max_length=20)
    application_type = models.CharField(max_length=20)
    institute_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    govt = models.BooleanField(default=False)
    program = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, null=True)
    intake = models.FloatField(default=60)