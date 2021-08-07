from django.contrib import admin
from posts.models import Post, Comment, Like

class AdminComment(admin.ModelAdmin):
    list_display = ['user', 'body']

class AdminLike(admin.ModelAdmin):
    list_display = ['user', 'post', 'value']  

admin.site.register(Post)
admin.site.register(Comment, AdminComment)
admin.site.register(Like, AdminLike)