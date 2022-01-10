from .forms import  *
from django.http import request
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile,Post
# Create your views here.
@login_required(login_url='/accounts/login/')

def logout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/accounts/login/')

def index(request):
    hoods =Neighbourhood.objects.all()
    business=Business.objects.all()
    context={
        'hoods':hoods,
        'business':business
    }
    return render(request,'index.html', context)

@login_required(login_url='/accounts/login/')

def update_profile(request):
    profile=Profile.objects.get(user=request.user) 
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('update')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile':profile,
    }
    
  
    return render(request, 'update_profile.html',context)
@login_required(login_url='/accounts/login/')

def profile(request):
    profile=Profile.objects.get(user=request.user)
    # print(user)
    
    ctx={
        'profile':profile,
    }
    return render(request, 'profile.html', ctx)
@login_required(login_url='/accounts/login/')

def new_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.save()
            return redirect('business')

    else:
        form = BusinessForm()
    return render(request, 'new_business.html', {'form': form})
@login_required(login_url='/accounts/login/')

def new_post(request):

    current_user = request.user
    # profile = request.user.email
 
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            # post.author_profile = profile
            post.save()
        return redirect('post')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})
@login_required(login_url='/accounts/login/')

def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "post":
        form = UpdatePostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = UpdatePostForm(instance=post)
            
    
    return render(request,'update_post.html',{'form':form})


@login_required(login_url='/accounts/login/')

def update_business(request, pk):
    business = Business.objects.get(pk=pk)
    if request.method == "post":
        form = UpdateBusinessForm(request.POST,request.FILES,instance=business)
        if form.is_valid():
            form.save()
            return redirect('business')
    else:
        form = UpdateBusinessForm(instance=business)
            
    
    return render(request,'update_business.html',{'form':form})

@login_required(login_url='/accounts/login/')

def get_post(request, pk):
	post = Post.objects.get(pk=pk)

	context = {
	'post':post
	}
	return render(request, 'detail_post.html', context)
@login_required(login_url='/accounts/login/')

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    
    
    return redirect('post')

@login_required(login_url='/accounts/login/')

def post(request):
    posts = Post.objects.all()
    
    return render(request, 'posts.html',{'posts':posts})
@login_required(login_url='/accounts/login/')

def business(request):
    businesses = Business.objects.all()
    
    return render(request, 'business.html',{'businesses':businesses})
@login_required(login_url='/accounts/login/')

def delete_business(request,pk):
    business = Business.objects.get(pk=pk)
    business.delete()
    
    
    return redirect('business')


@login_required(login_url='/accounts/login/')

def update(request):

	return render(request, 'update.html')

@login_required(login_url='/accounts/login/')

def category(request):
    # name=Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newhood')
            
    else:
        form = CategoryForm()
        
    return render(request, 'category.html', {'form':form})
@login_required(login_url='/accounts/login/')

def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
            return redirect('index')

    else:
        form = NeighbourHoodForm()
    return render(request, 'neighbourhood.html', {'form': form})
@login_required(login_url='/accounts/login/')

def hood(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request, 'index.html',{'hoods':hoods})
@login_required(login_url='/accounts/login/')

def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_businesses = Business.search_by_name(search_term)

        message = f"{search_term}"
        

        return render (request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
@login_required(login_url='/accounts/login/')

def detail(request):
    details = Neighbourhood.objects.all()
    
    return render(request, 'index.html',{'details':details})