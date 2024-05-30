from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.bloggen, name='bloggen'),
    path('generate_blog/', views.generate_blog, name='generate_blog')
    
]