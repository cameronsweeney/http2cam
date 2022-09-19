from .views import CamsDashboardView, CamsAppView, CamsModelView, CamsFileTreeView, CamsModelInstanceCRUDViewSet, CrispyFormTestView, CrispyFormSubmitView, latbEmailEndpointView
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('form/<contact_uuid>/eval', CrispyFormTestView.as_view()),
    path('form/<contact_uuid>/submit', CrispyFormSubmitView.as_view()),
    path('email/latb/<day>', latbEmailEndpointView.as_view()),
    path('app/<codename>', CamsAppView.as_view(), name='cams_app'),
    path('model/<codename>', CamsModelView.as_view(), name='cams_model'),
    path('tree/<codename>', CamsFileTreeView.as_view(), name='cams_filetree'),
    path('', CamsDashboardView.as_view(), name='cams_dashboard')
]

router = routers.SimpleRouter()
router.register('instance', CamsModelInstanceCRUDViewSet, basename='instance')

urlpatterns += router.urls
