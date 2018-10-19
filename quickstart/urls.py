from django.contrib import admin
from django.urls import path ,include
from django.conf.urls import url
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, schemas, renderers, response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from snippets import views as learn_views
from containers import obs_storage,qing_s2_test
import  token_certify,token_client
from rest_framework_swagger.views import get_swagger_view
from token_client import  SwaggerSchemaView

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User # 指定要序列化的模型
        fields = ('url', 'username', 'email', 'is_staff')# 指定要序列化的字段

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'snippets', learn_views.SnippetsViewSet)
# router.register(r'containers', obs_storage.OEContainers)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# generator = schemas.SchemaGenerator(title='Bookings API')

schema_view = get_swagger_view(title="S2 API")
# @api_view()
# @renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
# def schema_view(request):
#     generator = schemas.SchemaGenerator(title='Core API')
#     return response.Response(generator.get_schema(request=request))


urlpatterns = [
    # url('schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r"^docs/$", schema_view),
    url(r'^containers/', obs_storage.OEContainers.as_view()),
    url(r'^container/(?P<container_name>[^/]+)$', obs_storage.OEContainer.as_view()),

    url(r'^S2/create$', qing_s2_test.S2create.as_view()),
    url(r'^S2/describe$', qing_s2_test.S2Describe.as_view()),
    url(r'^S2/(?P<s2_id>[^/]+)$', qing_s2_test.S2.as_view()),
    url(r'^S2/resize/(?P<s2_id>[^/]+)$', qing_s2_test.S2resize.as_view()),
    url(r'^S2/poweron/(?P<s2_id>[^/]+)$', qing_s2_test.S2poweron.as_view()),
    url(r'^S2/poweroff/(?P<s2_id>[^/]+)$', qing_s2_test.S2poweroff.as_view()),
    url(r'^S2/update/(?P<s2_id>[^/]+)$', qing_s2_test.S2update.as_view()),
    url(r'^S2/change/(?P<s2_id>[^/]+)$', qing_s2_test.S2change.as_view()),
    url(r'^sharetarget$', qing_s2_test.S2ShareTarget.as_view()),
    url(r'^Sharetarget/enable/(?P<shared_targets>[^/]+)$', qing_s2_test.S2EnableShareTarget.as_view()),
    url(r'^Sharetarget/disable/(?P<shared_targets>[^/]+)$', qing_s2_test.S2DisableShareTarget.as_view()),
    url(r'^Sharetarget/modify$', qing_s2_test.S2ModifyShareTarget.as_view()),
    url(r'^Sharetarget/attach/(?P<shared_targets>[^/]+)$', qing_s2_test.S2AttachShareTarget.as_view()),
    url(r'^Sharetarget/detach/(?P<shared_targets>[^/]+)$', qing_s2_test.S2DetachShareTarget.as_view()),
    url(r'^Sharetarget/describeDefault$', qing_s2_test.S2DescribeDefaultParameters.as_view()),

    url(r'^NAS_Groups/create$', qing_s2_test.S2CreateGroups.as_view()),
    url(r'^NAS_Groups/describe$', qing_s2_test.S2DescribeGroups.as_view()),
    url(r'^NAS_Groups/modify$', qing_s2_test.S2ModifyGroups.as_view()),
    url(r'^NAS_Groups/delete/(?P<s2_group>[^/]+)$', qing_s2_test.S2DeletGroups.as_view()),

    url(r'^NAS_Account/create$', qing_s2_test.S2CreateAccount.as_view()),
    url(r'^NAS_Account/describe$', qing_s2_test.S2DescribeAccounts.as_view ()),
    url(r'^NAS_Account/modify$', qing_s2_test.S2ModifyAccounts.as_view ()),
    url(r'^NAS_Account/delete/(?P<s2_accounts>[^/]+)$', qing_s2_test.S2DeletAccount.as_view ()),

    url(r'^NAS_Associate/associate$', qing_s2_test.S2AssociateAccount.as_view ()),
    url(r'^NAS_Associate/dissociate$', qing_s2_test.S2DissociateAccount.as_view ()),

    url(r'^token_cerify/', token_certify.Token.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),# 用于前端的用户认证
    path ('admin/', admin.site.urls),
]

