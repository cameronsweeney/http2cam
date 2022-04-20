from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('home/', HomePageView.as_view(), name='home')
]