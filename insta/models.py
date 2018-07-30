from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
	status = HTMLField()
	profilepicture = models.ImageField(upload_to='images/', blank=True,default="/jVr43h8.png")
	secondary_email = models.CharField(max_length=100, null=True, blank=True)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
				UserProfile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

class Tags(models.Model):
	name = models.CharField(max_length=60,default="")