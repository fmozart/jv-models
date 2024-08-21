from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('all-news',views.all_news,name='all-news'),
    path('all-category',views.all_category,name='all-category'),
    path('detail/<int:id>',views.detail,name="detail"),
    path('category/<int:id>',views.category,name='category'),
 ]