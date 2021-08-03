from django.contrib import admin

# Register your models here.
from .models import Comment, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'status')
    list_filter = ('title', 'author', 'status')
    search_fields = ('title', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display= ('name','email', 'created_date', 'activate')
    list_filter= ('name','email', 'activate')
    search_fields= ('comment',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)