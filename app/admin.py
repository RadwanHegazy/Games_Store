from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group


admin.site.register(Category)
admin.site.register(Game)

admin.site.unregister(User)
admin.site.unregister(Group)
