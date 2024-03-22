from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=64, unique=True, null=True, blank=False)
    description = models.TextField(max_length=255, null=True, blank=False)
    user = models.ManyToManyField(User)
    
    def __str__(self) -> str:
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True, null=True, blank=False)
    text = models.TextField(max_length=1000, null=True, blank=False)
    date_of_create = models.DateTimeField (auto_now_add=True, null=True)
    date_of_update = models.DateTimeField (auto_now=True, null=True)
    topic = models.ManyToManyField(Topic, related_name='topic')
    user = models.ForeignKey(User, 
                             on_delete=models.DO_NOTHING,null=True, blank=False)
    
    def __str__(self) -> str:
        return f"{self.pk} - {self.title}"
    
class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, 
                                on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('Comment', 
                                null=True, 
                                blank=True, 
                                on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.ForeignKey(User, 
                             on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.text} by {self.user.username}"
