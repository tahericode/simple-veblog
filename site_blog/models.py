from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.shortcuts import reverse
from django.utils.translation import activate

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )


    title = models.CharField(max_length=150, unique=True, verbose_name='عنوان')
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.created_date.year,self.created_date.strftime('%m'),self.created_date.strftime('%d'),self.slug])
    
    def active_comment(self):
        return self.comment_set.filter(activate =True)


class Comment(models.Model):
    post = models.ForeignKey(Post,models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='نام ')
    email = models.EmailField( max_length=254, verbose_name='ایمیل')
    comment = models.CharField( max_length=500,verbose_name='کامنت')
    activate = models.BooleanField(verbose_name='فعال', default=False)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت کامنت')

    def __str__(self):
        return "{} by {} ".format(self.comment, self.name)
