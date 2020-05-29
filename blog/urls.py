from django.urls import path
from . import views

# This is just variable that use to clear the app name to Django
app_name = 'blog'

urlpatterns = [
    path('', views.all_blog, name= 'all_blog'),
    path('<int:blog_id>/', views.detail_view, name = 'detail')
]