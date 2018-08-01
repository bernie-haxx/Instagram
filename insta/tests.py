from django.test import TestCase
from .models import UserProfile,Tags,Image,Comments
import forgery_py
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class tagsTestClass(TestCase):
	def setUp(self):
		self.ben= Tags(name=forgery_py.name.first_name())

	def test_instance(self):
		self.assertTrue(isinstance(self.ben,Tags))	

	def test_save_method(self):
		self.ben.save_tags()
		tags = Tags.objects.all()
		self.assertTrue(len(tags)>0)

class UserProfileTestClass(TestCase):
	def test_profile_creation(self):
		Users = get_user_model()
		user = Users.objects.create(username="jeff", password="django-tutorial")
		self.assertIsInstance(user.profile, UserProfile)	
		user.save()
		self.assertIsInstance(user.profile, UserProfile)
		

