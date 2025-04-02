from django.contrib import admin
from .models import Post
from .models import Comment

admin.site.register(Post) # adds post table to admin page

admin.site.register(Comment) # adds new comment table to admin page
