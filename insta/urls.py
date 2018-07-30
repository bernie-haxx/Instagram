from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
url(r'^(?P<image_id>\d+)?$',views.home,name = 'welcome'),
url(r'^follow/(?P<other_user>\d+)',views.follow_function,name='follow'),
url(r'^unfollow/(?P<other_user>\d+)',views.unfollow_function,name='unfollow'),
url(r'^profile/(?P<user>\d+)',views.profile,name='profile'),
url(r'^profile/$',views.userprofile,name='current_profile'),
url(r'^otherprofile/(?P<others_user>\d+)$',views.otherprofile,name='other_profile'),
url(r'^new/profile$',views.new_profile,name='new-profile'),
url(r'^new/image$',views.new_image,name='new-image'),
]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)