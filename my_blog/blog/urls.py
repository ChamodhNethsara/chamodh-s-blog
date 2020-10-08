from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path("",views.welcome,name="welcome"),
    path("add_new_post/",views.new_post,name="new_post"),
    path("new/",views.new,name="new"),
    path('delete/<int:post_id>/',views.delete,name='delete'),
    path('view_post/<int:post_id>/',views.view_post,name='view_post'),
    path('add_comment/<int:post_id>/',views.add_comment, name= 'add_comment'),
    path('all_posts/',views.all_posts,name='all_posts'),
]