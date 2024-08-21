from django.contrib import admin
from newsapp.models import News, Comment, Category

# Register your models here.
class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time')
admin.site.register(News,AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display=('news','email','comment','status')
admin.site.register(Comment,AdminComment) 