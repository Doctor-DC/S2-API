from obs import ObsClient
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets
from django.http import JsonResponse
import json
# 创建ObsClient实例S
obsClient = ObsClient (
    access_key_id='GUPELS58GA5XK57ZMWFZ',
    secret_access_key='cNU11njXI2dN5Aylh9kYVo9dxZBZHKlEI6aHoWdj',
    server='https://obs.cn-north-1.myhwclouds.com'
)
# bucketClient = obsClient.bucketClient('dc-test')
# container_name = 'dc-obs-bucket-demo'


class OEContainers(APIView):
    def get(self, request):
        resp = obsClient.listBuckets ()
        print('common msg:status:', resp.status, ',errorCode:', resp.errorCode, ',errorMessage:', resp.errorMessage)
        msg = 'ok'
        return JsonResponse(resp.body, status=200)

    def post(self, request):
        kw = json.loads (request.body)['container']
        name = kw['name']
        bucketClient = obsClient.bucketClient (name)
        resp = bucketClient.createBucket ()
        return JsonResponse (resp.body, safe=False)

class OEContainer(APIView):

    def get(self, request, container_name):
        bucketClient = obsClient.bucketClient (container_name)
        res = bucketClient.getBucketLocation ()
        return JsonResponse (res.body, status=200)

    def delete(self, request, container_name):
        bucketClient = obsClient.bucketClient (container_name)
        res = bucketClient.deleteBucket ()
        return JsonResponse (res.status)

    def post(self, request,container_name):

        bucketClient = obsClient.bucketClient (container_name)
        resp = bucketClient.createBucket ()
        return JsonResponse (resp.body, safe=False)
