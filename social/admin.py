from django.contrib import admin

from social.models import Like, Post

admin.site.register(Post)
admin.site.register(Like)
