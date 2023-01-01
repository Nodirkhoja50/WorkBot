from django.urls import path
from .views import PostDetailView
urlpatterns = [
    path('',PostDetailView.as_view(),name='post'),
    path('url/<str:pk>/',PostDetailView.as_view(),name = 'url'),
    
]