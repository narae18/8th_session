from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    body = models.TextField()
    fanname = models.CharField(max_length=50)
    hashtag = models.CharField(max_length=50)
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    like = models.ManyToManyField(User, related_name='likes',blank=True)
    like_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
    


class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self) :
        return self.post.title+" : "+self.content[:20]
    

