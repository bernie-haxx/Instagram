from django.shortcuts import render,redirect,get_object_or_404,render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from friendship.models import Follow
from django.contrib import messages
from .models import UserProfile,Tags,Image,Comments
from .forms import NewProfileForm,NewCommentForm,NewImageForm
from django.http import HttpResponse,JsonResponse
# Create your views here.
@login_required(login_url='/accounts/register/')
def home(request,image_id=None):
	title='Home'
	discovers=UserProfile.objects.all()
	comments=Comments.objects.all()
	following=Follow.objects.following(request.user)
	images=Image.objects.all()
	message='Liking is by clicking on the picture'
	if image_id:
		image = get_object_or_404(Image, pk=image_id)
	images=[]
	for i in Follow.objects.following(request.user):
		images+=i.red.all()
	imagess=[]
	for b in Follow.objects.followers(request.user):
		imagess+=b.red.all()
	form = NewCommentForm()
	if image_id:
		image = get_object_or_404(Image, pk=image_id)
		if request.method == 'POST':
			commentform = NewCommentForm(request.POST)
			if commentform.is_valid():
				article = commentform.save(commit=False)
				article.user = request.user
				article.image = image
				article.save()
				return redirect('welcome')
	else:
			form = NewCommentForm()

	return render_to_response('home.html',locals())
	return render(request,'home.html',locals())



def profile(request,user):
	user=User.objects.get(id=user)
	profiles=UserProfile.objects.all()
	followers=len(Follow.objects.followers(request.user))
	following=len(Follow.objects.following(request.user))

	return render(request,'profile.html',locals())

@login_required(login_url='/accounts/login')
def follow_function(request,other_user):
	other_users=User.objects.get(id=other_user)
	addfollow=Follow.objects.add_follower(request.user, other_users)
	return redirect('welcome')

@login_required(login_url='/accounts/login')
def unfollow_function(request,other_user):
	other_users=User.objects.get(id=other_user)
	unfollow=Follow.objects.remove_follower(request.user, other_users)
	return redirect('welcome')

@login_required(login_url='/accounts/login')
def userprofile(request):
	followers=len(Follow.objects.followers(request.user))
	following=len(Follow.objects.following(request.user))
	image_count=len(Image.objects.filter(user_id=request.user.id))
	images=Image.objects.filter(user_id=request.user.id)
	message='Liking is by clicking on the picture'
	return render(request,'profile.html',locals())

@login_required(login_url='/accounts/login')
def otherprofile(request,others_user):
	followers=len(Follow.objects.followers(request.user))
	other_users=User.objects.get(id=others_user)
	following=len(Follow.objects.following(request.user))
	image_count=len(Image.objects.filter(user_id=other_users))
	images=Image.objects.filter(user_id=other_users)
	return render(request,'profile_other.html',locals())

@login_required(login_url='/accounts/login')
def new_profile(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('current_profile')

	else:
			form = NewProfileForm()
	return render(request, 'new_profile.html',{"form":form })

@login_required(login_url='/accounts/login')
def new_image(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewImageForm(request.POST,request.FILES)
		if form.is_valid():
			article = form.save(commit=False)
			article.user = current_user
			article.save()
			return redirect('current_profile')
	else:
			form = NewImageForm()
	return render(request, 'new_image.html',{"form":form })




@login_required(login_url='/accounts/login/')
def like(request, image_id):
	post = get_object_or_404(Image, pk=image_id)
	request.user.profile.like(post)
	return redirect('welcome')


def search_results(request):
	if 'title' in request.GET and request.GET["title"]:
		search_term = request.GET.get("title")
		searched_images = Image.search_by_title(search_term)
		message = f"{search_term}"
		return render(request,'search.html',{"message":message,"images":searched_images})
	else:
		message='You havent searched for any term'
		return render(request, 'search.html',locals())		
