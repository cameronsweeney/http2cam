from .views import CamsDashboardView, CamsAppView, CamsModelView, CamsFileTreeView
from django.urls import path

urlpatterns = [
    path('app/<codename>', CamsAppView.as_view(), name='cams_app'),
    path('model/<codename>', CamsModelView.as_view(), name='cams_model'),
    path('tree/<codename>', CamsFileTreeView.as_view(), name='cams_filetree'),
    path('', CamsDashboardView.as_view(), name='cams_dashboard')
]