#from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

#models.Model means that the Post is a Django Model
#so Django knows that it should be saved in the database.

#That means Model tells Django to store in a database and models is a self key to access the post  i.e our cls

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#link to another model
    title = models.CharField(max_length=200)#Limiting our title to 200 chara
    text = models.TextField()#Un limited txt field
    created_date = models.DateTimeField(default=timezone.now)#Default time
    published_date = models.DateTimeField(blank=True, null=True)#

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
