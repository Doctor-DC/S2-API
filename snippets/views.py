# from django.views.generic.base import View
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# class Snippetsdata(View):
#     def get(self, request):
#
#         return {'containers': containers, 'page_info': page_info}


from snippets.models import Snippets
from snippets.serializers import SnippetsSerializer

from rest_framework import viewsets


# Create your views here.
class SnippetsViewSet(viewsets.ModelViewSet):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsSerializer