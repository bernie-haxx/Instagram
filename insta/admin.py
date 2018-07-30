from django.contrib import admin
from .models import UserProfile,Tags,Image,Comments

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	filter_horizontal =('tags',)	
admin.site.register(UserProfile)
admin.site.register(Image,ImageAdmin)
admin.site.register(Tags)
admin.site.register(Comments)