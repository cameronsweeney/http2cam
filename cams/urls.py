from .views import CamsDashboardView, CamsAppView, CamsModelView, CamsFileTreeView, CamsModelInstanceCRUDView
from django.urls import path

urlpatterns = [
    path('crud/<pk>', CamsModelInstanceCRUDView.as_view(), name='cams_crud'),
    path('app/<codename>', CamsAppView.as_view(), name='cams_app'),
    path('model/<codename>', CamsModelView.as_view(), name='cams_model'),
    path('tree/<codename>', CamsFileTreeView.as_view(), name='cams_filetree'),
    path('', CamsDashboardView.as_view(), name='cams_dashboard')
]