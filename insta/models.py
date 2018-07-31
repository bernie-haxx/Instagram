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


	def like(self, photo):
		if self.mylikes.filter(photo=photo).count() == 0:
			Likes(photo=photo,user=self).save()

class Tags(models.Model):
	name = models.CharField(max_length=60,default="")
class Image(models.Model):
	image=models.ImageField(upload_to='images/', blank=True)
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name="red")
	title = models.CharField(max_length=60, null=True)
	time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
	time_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_uploaded = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default=0)
	caption = models.CharField(max_length=140, default="")
	tags = models.ManyToManyField(Tags,related_name="tags",blank=True)

	@property
	def get_comments(self):
		return self.comments.all()
	

class Comments(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name='user')
	comments = models.TextField()
	date_posted = models.DateTimeField(auto_now=True)
	image=models.ForeignKey(Image, on_delete=models.CASCADE,related_name="comments")