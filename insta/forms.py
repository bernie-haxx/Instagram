from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile,Comments,Image
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user'] 


class NewCommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('comments',)        


class NewImageForm(forms.ModelForm):
	class Meta:
		model = Image
		exclude = ['user','time_created','time_updated','date_uploaded','likes','tags']		

