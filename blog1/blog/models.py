from django.db import models

# Create your models here.
from django.urls import reverse
class Topic(models.Model):
    topic = models.CharField(max_length=20)
    def __str__(self):
        return self.topic 
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        "auth.User", # this provides for user authentication
        on_delete=models.CASCADE, 
        )
    body = models.TextField()
    def __str__(self): # this provides for a readable model in the admin shell
        return self.title
    def get_absolute_url(self): # this builds a URL address for a model object
        return reverse("post_detail", kwargs={"pk": self.pk}) 
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT,default='1')
    date = models.DateField(auto_now_add=True, )
    image = models.ImageField(null=True, blank=True,
    upload_to="images/")


       

