from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.gis.db import models #not typical django model
from django.contrib.auth.models import User



# Create your models here.

class Washroom(models.Model):
	name = models.CharField(max_length=50)
	rating = models.FloatField(null=True)
	disable_access=models.BooleanField(default=False) #disable
	unisex = models.CharField(max_length=30, default='False')
	location = models.PointField()
	id = models.BigIntegerField(primary_key=True)
	type = models.CharField(max_length=30, default='unknown')
	access = models.CharField(max_length=30, default='False')
	indoor = models.CharField(max_length=30, default='False')
	diaper = models.CharField(max_length=30, default='False')
	water = models.CharField(max_length=30, default='False')
	wheelchair = models.CharField(max_length=30, default='False')
	opening_hours = models.CharField(max_length=50, default="")
	
	def get_absolute_url(self):
		return "/washrooms/%d" % self.id



class Review(models.Model): #many reviews to one washroom relationship
	washroom = models.ForeignKey(Washroom, on_delete=models.CASCADE)
	rating = models.FloatField()
	comment = models.CharField(max_length=100)

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
