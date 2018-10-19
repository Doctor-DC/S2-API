import coreapi
import jwt
from jwt import DecodeError
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView
from django.http import JsonResponse
import json
import requests

class Token(APIView):
    def post(self,  request):
        key = request.POST['key']
        token = request.POST['token']
        decoded = jwt.decode(token, key, False)
        # sub = (decoded['sub'])
        # username = (decoded['username'])
        # print(sub)
        return JsonResponse(decoded)


    def get(self,  request):

        token = request.META.get('HTTP_TOKEN', None)
        # token = request.GET.get('HTTP_TOKEN', '')
        # key = request.GET.get('key', '1')
        decoded = jwt.decode(token,None, False)

        return JsonResponse(decoded)

# key = None
# token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjbXBfYWRtaW4iLCJwaG9uZSI6IiIsIm9yZ0NvZGUiOjEwMDAwMSwiZXhwIjoxNTM4MDMyMjU0LCJ1dWlkIjoiNDI3YWIwMDgtZTk4Zi00ZjUzLWIzZDctOTJkZTFhNGQ4OTNkIiwiZW1haWwiOiIiLCJhdXRob3JpdGllcyI6WyJST0xFX1NZUyIsIkNNUF9DTVBfQURNSU4iLCJCTVNfU1lTIl0sInJlc291cmNlQ29kZXMiOltdLCJ1c2VybmFtZSI6ImNtcF9hZG1pbiJ9.0vd7geH5sqEVPExekV36kcZ8uwcc_FlztlB2RSIlvafuIDE628ulEBwldKitnqQQhCRCJnCXjBLEShNfdqAXYQ'
# certify_token(key,token)

def token_certify_decorator(func):
    def wrapper(request, *args, **kwargs):
        token = request.META.get ('HTTP_AUTHORIZATION', None)
        decoded = jwt.decode (token, None, False)

        # return JsonResponse (decoded)
        return func(request, *args, **kwargs)
    return wrapper

def DocParams(name):
    def coreapi_decorator(func):
        def wrapper( *args, **kwargs):
            schema = AutoSchema (
                manual_fields=[
                    coreapi.Field (name=name, required=True, location='header', description='', type='string'),


                ]
            )

        return wrapper
    return coreapi_decorator