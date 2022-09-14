# cams/views.py
from rest_framework import generics, response, status
from drf_multiple_model import views
from . import models, serializers, permissions


class CamsDashboardView(generics.ListAPIView):
    def get_queryset(self):
        authorized_apps = models.CamsAppAuthorization.objects.select_related('app').filter(user=self.request.user.id)
        return authorized_apps

    def list(self, request):
        if not request.user.is_authenticated:
            content = {'detail': 'Please log in with a valid CAMS account.'}
            return response.Response(content, status=status.HTTP_403_FORBIDDEN)
        return response.Response(serializers.AppViewSerializer(self.get_queryset(), many=True).data)

class CamsAppView(views.ObjectMultipleModelAPIView):
    permission_classes = [permissions.CamsAppPermission]

    def get_queryset(self):
        self.queryset = models.CamsApp.objects.filter(codename=self.kwargs['codename'])
        return self.queryset

    def get(self, request, *args, **kwargs):
        self.check_object_permissions(self.request, kwargs['codename'])
        return self.list(request, *args, **kwargs)

    def get_querylist(self):
        app_name = self.kwargs['codename']
        querylist = [        # later, add another query for associated apps
            {
                'queryset': models.CamsModel.objects.filter(app=app_name),
                'serializer_class': serializers.CamsModelSerializer,
                'label': 'models'
            },
            {
                'queryset': models.CamsActionGlobal.objects.filter(app=app_name),
                'serializer_class': serializers.CamsActionSerializer,
                'label': 'actions'
            },
            {
                'queryset': models.CamsFileTree.objects.filter(app=app_name),
                'serializer_class': serializers.CamsFileTreeSerializer,
                'label': 'filetrees'
            }

        ]
        return querylist

class CamsModelView(views.ObjectMultipleModelAPIView):
    permission_classes = [permissions.CamsModelPermission]
        
    def get_queryset(self):
        self.queryset = models.CamsModel.objects.filter(codename=self.kwargs['codename'])
        return self.queryset

    def get(self, request, *args, **kwargs):
        self.check_object_permissions(self.request, kwargs['codename'])
        return self.list(request, *args, **kwargs)

    def get_querylist(self):
        model_name = self.kwargs['codename']
        querylist = [
            {
                'queryset': models.CamsModelInstance.objects.filter(cams_model=model_name),
                'serializer_class': serializers.CamsModelInstanceSerializer,
                'label': f'{model_name}/model'
            },
            {
                'queryset': models.CamsActionLocal.objects.filter(cams_model=model_name),
                'serializer_class': serializers.CamsActionSerializer,
                'label': f'{model_name}/action'
            }
        ]
        return querylist

class CamsFileTreeView(generics.ListAPIView):
    permission_classes = [permissions.CamsFileTreePermission]
    serializer_class = serializers.CamsModelInstanceSerializer

    def get_queryset(self):
        filetree_name = self.kwargs['codename']
        self.queryset = models.CamsModelInstance.objects.filter(filepath__startswith=filetree_name)
        return self.queryset

    def get(self, request, *args, **kwargs):
        self.check_object_permissions(self.request, kwargs['codename'])
        return self.list(request, *args, **kwargs)

class CamsModelInstanceCRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.CamsCRUDPermission]
    queryset = models.CamsModelInstance.objects.select_related('cams_model__app').all()
    serializer_class = serializers.CamsModelInstanceSerializer