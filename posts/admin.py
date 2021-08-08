from django.contrib import admin
from posts.models import Post, Comment, Like, Tips

class AdminComment(admin.ModelAdmin):
    list_display = ['user', 'body']

class AdminLike(admin.ModelAdmin):
    list_display = ['user', 'post', 'value']  

class AdminTips(admin.ModelAdmin):
    list_display = ['topic', 'author', 'created']

admin.site.register(Post)
admin.site.register(Comment, AdminComment)
admin.site.register(Like, AdminLike)
admin.site.register(Tips, AdminTips)