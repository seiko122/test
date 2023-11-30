from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='f10ff70a7155e5ab666bcdd1b45b726d.jpg',upload_to='profile_pics')
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Images(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(null=True,blank=True,max_length=200)
status=(
    ('games','games'),
    ('consoles','consoles'),
    ('controllers','controllers'),
    ('accessories','accessories'),
)
class Product(models.Model):
    title = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='productsimages')
    description = models.TextField()
    price = models.FloatField(default=0)
    discount = models.FloatField(null=True,blank=True)
    status = models.CharField(max_length=200,choices=status)
    count = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)
    is_sale = models.BooleanField(default=False)
    