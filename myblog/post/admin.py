from django.contrib import admin

from .models import Post, Comment

admin_show_models = [Post, Comment]
admin.site.register(admin_show_models)