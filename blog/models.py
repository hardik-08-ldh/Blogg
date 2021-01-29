from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def  get_absolute_url(self):
       
        return reverse('home')

class Profile(models.Model):
   
    user =models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True ,blank=True,upload_to="images/profile")
    linkedin_url=models.CharField(max_length=255 , null=True , blank=True)
    codechef_url=models.CharField(max_length=255 , null=True , blank=True)
    codeforces_url=models.CharField(max_length=255 , null=True , blank=True)

    def __str__(self):
        return str(self.user)

    def  get_absolute_url(self):
        return reverse('home')
class Post(models.Model):
    title=models.CharField(max_length=200)
    header_image=models.ImageField(null=True ,blank=True,upload_to="images/")
   
    author=models.ForeignKey(User,on_delete=models.CASCADE)
   
    body=RichTextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100,default='coding')
    snippet=models.CharField(max_length=255,default='Click The Link Above To Head To The Post')
    like=models.ManyToManyField(User,related_name='blog_posts')
    
    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title+'-'+str(self.author)

    def  get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    body=models.TextField()
    name_of_user=models.CharField(max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post) +' by- ' +str(self.name_of_user)

    class Meta:
        ordering=('-date_added',)