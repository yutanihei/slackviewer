from django.contrib import admin
from .models import Post, Channel, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Channel)
admin.site.register(User)