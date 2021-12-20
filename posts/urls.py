from django.urls import path
from . import views

urlpatterns = [
    path('new_post/', views.new_post, name='new_post'),
    path('view_post/', views.view_post, name='view_post'),
    path('view_post/<int:id>', views.view_post_details, name='view_post_details'),
    path('search/', views.search, name='search')
]
