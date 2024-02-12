from django.urls import path
from .views import index, main_post, main_detail

urlpatterns = [
    path('', index, name='main_page'),
    path('main-post/', main_post, name='main_post'),
    path('route/<int:pk>', main_detail, name='main_detail'),
    ]