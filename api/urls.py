from django.urls import path

from .views import ApiPostView,DetailPost

urlpatterns =[
    path('',ApiPostView.as_view(),name='api_post'),
    path('<int:pk>/',DetailPost.as_view())
]