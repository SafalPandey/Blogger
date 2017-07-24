from django.contrib import admin
from .models import post

admin.site.site_header = "Blogger User Panel"
# Register your models here.
admin.site.register(post)
