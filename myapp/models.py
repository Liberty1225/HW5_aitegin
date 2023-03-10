from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    fullname = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.fullname


class Mentor(models.Model):
    fullname = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.fullname
