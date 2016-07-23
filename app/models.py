from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BbsUser (models.Model):

    user=models.OneToOneField(User)
    #name=models.CharField(max_length=32,unique=True)
    signature=models.CharField(max_length=128,default="The guy leave nothing")
    icon =models.ImageField(upload_to='upload_imgs/',default="upload_imgs/nicai.jpg")

    def __str__(self):   # or __unicode__
        return '%s'%self.user


class Bbs (models.Model):

    title=models.CharField(max_length=80)
    category=models.ForeignKey('Category')
    content=models.TextField()
    author=models.ForeignKey('BbsUser')
    view_count=models.IntegerField()
    ranking=models.IntegerField()
    create_at=models.DateTimeField(auto_now_add=True,editable=True)
    update_at=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Like(models.Model):
    to_bbs=models.ForeignKey(Bbs)
    like_num=models.IntegerField(default=0)

class Category (models.Model):

    name=models.CharField(max_length=32,unique=True)

    def __unicode__(self):
        return self.name
    class Meta:
        ordering=['id']





