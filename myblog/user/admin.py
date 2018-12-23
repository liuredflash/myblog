from django.contrib import admin

from .models import User

admin_show_models = [User]

admin.site.register(admin_show_models)