from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy


@api_view(['GET'])
def api_root(request):


    return Response({
        # users endpoints
        'users': reverse('users-api:users', request=request),
        'register': reverse('users-api:register', request=request),
        'login': reverse('users-api:login', request=request),
        'profile_update': reverse('users-api:profile_update', request=request),
        })
