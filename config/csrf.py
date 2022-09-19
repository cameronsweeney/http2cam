# an endpoint specifically to GET a CSRF token, which will enable login with POST
# https://fractalideas.com/blog/making-react-and-django-play-well-together-single-page-app-model/

from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import views, response, status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

class GetCSRFTokenView(views.APIView):
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        # return JsonResponse({'csrfToken': get_token(request)})
        return response.Response(status=status.HTTP_204_NO_CONTENT)

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})