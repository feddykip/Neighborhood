from django import forms
from django.contrib.auth.models import User
from .models import Profile,Business,Post,Category,Neighbourhood

# class UserProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ('user_name','bio','image')


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields=['name']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.FileField()

    class Meta:
        model = Profile
        fields = ['image','website_url',
        'phone_number','instagram_url','facebook_url','neighbourhood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'created', 'user_profile', 'image']
        widgets = {
          'location': forms.Textarea(attrs={'rows':1, 'cols':10,}),
        }

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
      
        exclude = ['author', 'created', 'author_profile', 'neighbourhood',]
        widgets = {
          'post': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }

class UpdatePostForm(forms.ModelForm):
   class Meta:
        model = Post
      
        exclude = ['author', 'created', 'author_profile', 'neighbourhood',]
        widgets = {
          'post': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }


class UpdateBusinessForm(forms.ModelForm):
   class Meta:
        model = Business
      
        exclude = ['user', 'created', 'user_profile', 'image']
        widgets = {
        'location': forms.Textarea(attrs={'rows':1, 'cols':10,}),
        }