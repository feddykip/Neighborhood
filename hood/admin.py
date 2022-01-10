from django.contrib import admin
from .models import Profile,Category,Neighbourhood,Post,Business
# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Neighbourhood)
admin.site.register(Post)
admin.site.register(Business)