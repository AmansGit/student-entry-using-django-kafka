from django.db import models

# Create your models here.
class Student(models.Model):
	id = models.AutoField(primary_key=True)
	f_name = models.CharField(max_length=20, null=False)
	l_name = models.CharField(max_length=20, null=True)
	roll_no = models.IntegerField()
	date_joining = models.DateTimeField()
	created_by = models.ForeignKey(RootUser, on_delete=models.CASCADE)

	def __str__(self):
        return self.f_name


class RootUser(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=10, null=False)

	def __str__(self):
        return self.name