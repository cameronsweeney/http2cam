from .views import CamsDashboardView, CamsAppView, CamsModelView, CamsFileTreeView, CamsModelInstanceCRUDViewSet, CrispyFormTestView, CrispyFormSubmitView, latbEmailEndpointView
from .reports import LatbEvalReportView
from django.urls import path
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('LectureattheBeach/<contact_uuid>/eval', csrf_exempt(CrispyFormTestView.as_view())),
    path('LectureattheBeach/<contact_uuid>/submit', csrf_exempt(CrispyFormSubmitView.as_view())),
    path('LectureattheBeach/email/<day>', latbEmailEndpointView.as_view()),
    path('LectureattheBeach/report', LatbEvalReportView.as_view()),
    path('app/<codename>', CamsAppView.as_view(), name='cams_app'),
    path('model/<codename>', CamsModelView.as_view(), name='cams_model'),
    path('tree/<codename>', CamsFileTreeView.as_view(), name='cams_filetree'),
    path('', CamsDashboardView.as_view(), name='cams_dashboard')
]

router = routers.SimpleRouter()
router.register('instance', CamsModelInstanceCRUDViewSet, basename='instance')

urlpatterns += router.urls
