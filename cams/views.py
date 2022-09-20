# cams/views.py
from rest_framework import generics, response, status, viewsets
from drf_multiple_model import views
from . import models, serializers, permissions, forms, emails
from django.views.generic import TemplateView, View
from django.template.response import TemplateResponse
from django.http import JsonResponse

questionnaires_by_day = {
    "Wednesday": forms.latbWedForm,
    "Thursday": forms.latbThursForm,
    "Friday": forms.latbFriForm,
    "Saturday": forms.latbSatForm
}

dates_by_day = {
    "Wednesday": "21st",
    "Thursday": "22nd",
    "Friday": "23rd",
    "Saturday": "24th"
}

class CrispyFormTestView(TemplateView):
    template_name = 'questionnaire.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = models.CamsModelInstance.objects.filter(id=context['contact_uuid']).get()
        for day in ['Wednesday', 'Thursday', 'Friday', 'Saturday']:
            if day in self.request.GET:
                context['day'] = day
                break
        context['form'] = questionnaires_by_day[context['day']]
        context['datestring'] = f"{context['day']}, September {dates_by_day[context['day']]}, 2022"
        context['email'] = context['user']['E-mail Address']
        return context

class CrispyFormSubmitView(View):
    template_name = 'submit.html'
    def post(self, request, *args, **kwargs):
        print(request)
        db_objects = models.CamsFormResponse.objects.create(response_data=request.POST.dict())
        return TemplateResponse(request, 'submit.html', request.POST.dict())

class latbEmailEndpointView(generics.RetrieveAPIView):
    permission_classes = [permissions.CamsAppPermission]

    def get_queryset(self):
        if self.kwargs['day'] in ('Wednesday', 'Thursday', 'Friday', 'Saturday'):
            one_kwarg = {f"content__{self.kwargs['day']}__in": ['on', 'true', 'True', True]}
            queryset = models.CamsModelInstance.objects.filter(cams_model='contact', **one_kwarg)
        else:
            queryset = None
        self.queryset = queryset
        return queryset

    def get(self, request, *args, **kwargs):
        self.check_object_permissions(self.request, 'latb22')
        queryset = self.get_queryset()
        data = {'day': kwargs['day'], 'queried': list(queryset.values())}
        print(data)
        emails.mailMergeByDay(data)
        return JsonResponse(data, safe=False)

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
                'label': 'instances'
            },
            {
                'queryset': models.CamsActionLocal.objects.filter(cams_model=model_name),
                'serializer_class': serializers.CamsActionSerializer,
                'label': 'actions'
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

class CamsModelInstanceCRUDViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.CamsCRUDPermission]
    queryset = models.CamsModelInstance.objects.select_related('cams_model__app').all()
    serializer_class = serializers.CamsModelInstanceSerializer