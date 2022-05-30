from django.contrib import admin
from . import models

from user.models import User


class Users(admin.ModelAdmin):
  list_display = ('id', 'name', 'email')
  list_display_links = ('id', 'name', 'email')


admin.site.register(User, Users)
