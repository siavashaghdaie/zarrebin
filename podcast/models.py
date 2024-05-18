from email import message
from re import T
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Podcaster(models.Model):
    personId = models.IntegerField(verbose_name='شماره')
    firstName = models.CharField(max_length=25, verbose_name='نام');
    lastName = models.CharField(max_length=25,verbose_name='نام خانوادگی');
    position = models.CharField(max_length=25,verbose_name='مسئولیت');
    about = models.TextField(verbose_name='درباره ی من');
    pic = models.ImageField(verbose_name='تصویر')
    def __str__(self) -> str:
        return self.firstName;


class Podcast(models.Model):
    name = models.CharField(max_length=25, verbose_name='نام')
    description = models.TextField(verbose_name='درباره‌ی اپیزود')
    highlights = models.TextField(verbose_name='جان مایه')
    publishDate=models.DateField(verbose_name='تاریخ', auto_now=True)
    episodeNum = models.IntegerField(verbose_name='شماره ی اپیزود')
    producer = models.ForeignKey (Podcaster, on_delete=models.SET_NULL, null=True, verbose_name='تهیه کننده')
    cast = models.TextField(verbose_name='عوامل', null=True)
    music = models.TextField(verbose_name='موسیقی ها', null=True)
    pic = models.ImageField(null=True,blank=True,upload_to='images/', verbose_name='تصویر')
    text = models.TextField(verbose_name='متن', null=True)
    castboxlink = models.TextField(verbose_name='لینک کست باکس', null=True)
    castboxilink = models.TextField(verbose_name='لینک آی فریم کست باکس', null=True)

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    sender = models.CharField(max_length=25, verbose_name='ارسال کننده');
    subject = models.CharField(max_length=50, verbose_name='موضوع');
    message = models.TextField(verbose_name='پیام');

 