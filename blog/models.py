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
        # return reverse('article', args=str(self.pk))
        return reverse('home')

class Profile(models.Model):
    # \/ we described a new claa for profile page as it is added afterwards to the project
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
    # /\ we will not put the image in database but only the location of it uploaded to"image dir" next setup in settings.py file
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # body=models.TextField()
    body=RichTextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100,default='coding')
    snippet=models.CharField(max_length=255,default='Click The Link Above To Head To The Post')
    like=models.ManyToManyField(User,related_name='blog_posts')
    # /|\ makes a new table blog_post_like in database
    # The related_name attribute specifies the name of the reverse relation from the User model back to your model.
# If you don't specify a related_name, Django automatically creates one using the name of your model with the suffix _set
# , for instance User.map_set.all().
# If you do specify, e.g. related_name=maps on the User model, User.map_set will still work,
#  but the User.maps. syntax is obviously a bit cleaner and less clunky; so for example,
#  if you had a user object current_user, you could use current_user.maps.all()
#  to get all instances of your Map model that have a relation to current_user.
# .pragma table_info('tablename') can be used to see about tables

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title+'-'+str(self.author)

    def  get_absolute_url(self):
        # return reverse('article', args=str(self.pk))
        return reverse('home')