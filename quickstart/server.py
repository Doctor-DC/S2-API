from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_charm(request):
    print(request.user , request.user.id)
    return HttpResponse("Welcome.")



