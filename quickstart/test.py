# from django.http import HttpResponse
# from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
#
# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
# def get_charm(request):
#     print(request.user , request.user.id)
#     return HttpResponse("Welcome.")
#
#
import requests

url="http://127.0.0.1:8000/users"
# headers={'Authorization': ''}

r = requests.get(url)

print(r.status_code)
print(r.json)
print(r.text)



#
