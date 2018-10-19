import coreapi
import coreschema
import qingcloud.iaas
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.schemas import AutoSchema
from rest_framework.utils import json
from rest_framework.views import APIView
# from json_schema_generator import SchemaGenerator
from rest_framework.viewsets import ViewSetMixin
from token_certify import token_certify_decorator, DocParams

conn = qingcloud.iaas.connect_to_zone(
 'LFRZ1', # 你的资源所在的节点ID，可在控制台切换节点的地方查看，如 'pek1', 'pek2', 'gd1' 等
 'BGXPSXMWJLTAYLFKBDPE',
 'Kjf2nCzzMuRrHXV0VpuXSZhoMktLTuzXgrPzsozV',
 False
 )

def DocParam(name="default", location="query",
             required=True, description=None, type="string",
             *args, **kwargs):
    # return coreapi.Field(name=name, location=location,
    #                      required=required, description=description,
    #                      type=type)
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name=name, location=location,
                           required=required, description=description,
                           type=type)
        ]
    )
    print(schema)
    return schema


class S2create (APIView):
    """
    post:
         创建共享存储器
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='vxnet', required=True, location='query', description='', type='string'),
            coreapi.Field (name='service_type', required=True, location='query', description='', type='string'),
        ]
    )
    def post(self, request):
        vxnet = request.GET.get ('vxnet', '')           #字符串Query String参数
        service_type = request.GET.get ('service_type', '')
        S2_SAN = conn.create_s2_server(vxnet,service_type)
        return JsonResponse(S2_SAN, status=200)

class S2Describe(APIView):
    """
    get:
        获取共享存储服务器
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='s2_id', required=False, location='query', description='', type='string'),
        ]
    )
    @method_decorator (token_certify_decorator)
    def get(self, request):  # 获取查询列表
        s2_id = request.GET.get('s2_id')
        if s2_id is None:
            pass
        else:
            s2_id = s2_id.split()
        # service_types = request.GET.get ('service_types')
        S2_SAN = conn.describe_s2_servers (s2_servers=s2_id)
        return JsonResponse (S2_SAN, status=200)

# @method_decorator(token_certify_decorator, name='put','get')
class S2(APIView):
    """
    delete:
         删除共享存储服务器
    put:
         修改共享存储服务器属性
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='s2_server_name', required=False, location='query', description='', type='string'),
            coreapi.Field (name='description', required=False, location='query', description='', type='string')
        ]
    )
    @method_decorator (token_certify_decorator)
    def put(self, request,s2_id):                   #修改名称或描述
                                                                        # body = json.loads (request.body)['container']
        s2_server_name = request.GET.get('s2_server_name')                 # name = body['name']
        description = request.GET.get('description')                                                            # description = body['description']
        S2_SAN = conn.modify_s2_server(s2_id,s2_server_name,description)
        return JsonResponse(S2_SAN, status=200)

    @method_decorator (token_certify_decorator)
    def delete(self,request,s2_id):
        S2_SAN = conn.delete_s2_servers (s2_servers=[s2_id])
        return JsonResponse (S2_SAN, status=200)

class S2resize (APIView):
    """
    put:
         修改共享存储服务器的类型
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='server_type', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request,s2_id):
        if s2_id is None:
            pass
        else:
            s2_id = s2_id.split()
        server_type = request.GET.get('server_type')
        S2 = conn.resize_s2_servers(s2_id,server_type)
        return JsonResponse(S2)

class S2poweron (APIView):
    """
    put:
         启动S2
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            # coreapi.Field (name='server_type', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request, s2_id):

         s2_id = s2_id.split()
         S2_SAN = conn.poweron_s2_servers(s2_servers=s2_id)
         return JsonResponse (S2_SAN, status=200)


class S2poweroff (APIView):
    """
        put:
             关闭S2
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            # coreapi.Field (name='server_type', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request, s2_id):
        s2_id = s2_id.split ()
        S2_SAN = conn.poweroff_s2_servers (s2_servers=s2_id)
        return JsonResponse (S2_SAN, status=200)

class S2update (APIView):
     """
     put:
          s2 更新应用修改
     """
     schema = AutoSchema (
         manual_fields=[
             coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
             # coreapi.Field (name='server_type', required=False, location='query', description='', type='string'),
         ]
     )

     @method_decorator (token_certify_decorator)
     def put(self, request, s2_id):
         s2_id = s2_id.split ()
         S2_SAN = conn.update_s2_servers (s2_servers=s2_id)
         return JsonResponse (S2_SAN, status=200)


class S2change ( APIView):
    """
    put:
         修改共享存储服务器绑定的私有网络
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='vxnet', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request, s2_id):
        # body = json.loads (request.body)['container']
        # vxnet = body['vxnet']
        vxnet = request.GET.get('vxnet')
        S2_SAN = conn.change_s2_server_vxnet (s2_id,vxnet)
        return JsonResponse (S2_SAN, status=200)

class S2ShareTarget (APIView):
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='vxnet', required=False, location='query', description='', type='string'),
        ]
    )
    def post(self, request):

         body = json.loads (request.body,strict=False)['container']
         s2_id = body['s2_id']
         export_name = body['export_name']
         target_type = body['target_type']
         S2_SAN = conn.create_s2_shared_target(s2_id,export_name,target_type)
         return JsonResponse(S2_SAN, status=200)

    def get(self, request):  # 获取查询列表 多条件应尝试body
         S2_ID = request.GET.get('s2_server_id')
         shared_targets = request.GET.get('shared_targets')
         S2_SAN = conn.describe_s2_shared_targets(s2_server_id=[S2_ID])
         return JsonResponse (S2_SAN, status=200)

    def delete(self, request):
         body = json.loads (request.body)['container']
         shared_target= body['shared_target']
         S2_SAN = conn.delete_s2_shared_targets([shared_target])
         return JsonResponse (S2_SAN, status=200)

class S2EnableShareTarget (APIView):
    """
    put:
         启动目标门户组
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self,request,shared_targets):
        shared_targets = shared_targets.split()
        S2 = conn.enable_s2_shared_targets(shared_targets)
        return JsonResponse(S2)


class S2DisableShareTarget (APIView):
    """
    put:
         禁用目标门户组
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request, shared_targets):
        shared_targets = shared_targets.split ()
        S2 = conn.disable_s2_shared_targets (shared_targets)
        return JsonResponse (S2)

class S2ModifyShareTarget (APIView):
    """
    put:
         修改共享存储目标属性(vnas目录)
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='shared_targets', required=False, location='query', description='', type='string'),
            coreapi.Field (name='export_name', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request,):
        operation = request.GET.get('operation')
        shared_targets = request.GET.get('shared_targets')
        export_name = request.GET.get('export_name')
        S2 = conn.modify_s2_shared_target_attributes(shared_target=shared_targets,operation='modify',export_name=export_name)
        return JsonResponse (S2)

class S2AttachShareTarget (APIView):
    """
     put:
          共享存储目标添加硬盘
     """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='volumes', required=True, location='query', description='', type='string'),
            # coreapi.Field (name='export_name', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request, shared_targets):
        volumes = request.GET.get('volumes')
        volumes = volumes.split()
        S2 = conn.attach_to_s2_shared_target(shared_target=shared_targets,volumes=volumes)
        return JsonResponse (S2)

class S2DetachShareTarget (APIView):
    """
        put:
             共享存储目标卸载硬盘
        """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='volumes', required=True, location='query', description='', type='string'),
            # coreapi.Field (name='export_name', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request, shared_targets):
        volumes = request.GET.get('volumes')
        volumes = volumes.split ()
        S2 = conn.detach_from_s2_shared_target(shared_target=shared_targets,volumes=volumes)
        return JsonResponse (S2)

class S2DescribeDefaultParameters (APIView):
    """
    get:
         获取共享存储目标缺省参数
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='service_type', required=False, location='query', description='', type='string'),
            coreapi.Field (name='target_type', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def get(self, request):  # 获取查询列表 多条件应尝试body

        service_type = request.GET.get ('service_type')
        target_type = request.GET.get('target_type')
        S2_SAN = conn.describe_s2_default_parameters(service_type,target_type)
        return JsonResponse (S2_SAN, status=200)

class S2CreateGroups (APIView):
    """
    post:
          创建NAS权限组
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='group_type', required=True, location='query', description='', type='string'),
            # coreapi.Field (name='export_name', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def post(self, request):
        group_type = request.GET.get ('group_type')
        group_name = request.GET.get('group_name')
        description = request.GET.get('description')
        S2_SAN = conn.create_s2_group(group_type=group_type,group_name=group_name)
        return JsonResponse (S2_SAN, status=200)

class S2DescribeGroups (APIView):
    """
       get:
            查询权限组
       """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='group_id', required=False, location='query', description='', type='string'),
            # coreapi.Field (name='export_name', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def get(self, request):  # 获取查询列表 多条件应尝试body

        s2_groups = request.GET.get ('group_id')
        if s2_groups is None:
             pass
        else:
             s2_groups = s2_groups.split()
        S2_SAN = conn.describe_s2_groups(s2_groups)
        return JsonResponse (S2_SAN, status=200)

class S2ModifyGroups (APIView):
    """
    put:
          修改权限组属性
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='s2_group', required=True, location='query', description='', type='string'),
            coreapi.Field (name='group_name', required=False, location='query', description='', type='string'),
            coreapi.Field (name='description', required=False, location='query', description='', type='string'),
            # coreapi.Field (name='export_name', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request):

        s2_group = request.GET.get ('s2_group')
        group_name = request.GET.get('group_name')
        description = request.GET.get('description')
        S2_SAN = conn.modify_s2_group(s2_group=s2_group,group_name=group_name,description=description)
        return JsonResponse (S2_SAN, status=200)

class S2DeletGroups (APIView):
    """
    delete:
              删除权限组
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),

        ]
    )

    @method_decorator (token_certify_decorator)
    def delete(self, request,s2_group):
        s2_groups = s2_group.split()
        S2_SAN = conn.delete_s2_group(s2_groups=s2_groups)
        return JsonResponse (S2_SAN)


class S2CreateAccount (APIView):
    """
    post:
          创建NAS账户
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='account_type', required=True, location='query', description='', type='string'),
            coreapi.Field (name='account_name', required=False, location='query', description='', type='string'),
            coreapi.Field (name='nfs_ipaddr', required=False, location='query', description='', type='string'),
            coreapi.Field (name='smb_name', required=False, location='query', description='', type='string'),
            coreapi.Field (name='smb_passwd', required=False, location='query', description='', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def post(self, request):
        account_type = request.GET.get('account_type')
        account_name = request.GET.get('account_name')
        nfs_ipaddr = request.GET.get('nfs_ipaddr')
        smb_name = request.GET.get('smb_name')
        smb_passwd = request.GET.get('smb_passwd')
        S2_SAN = conn.create_s2_account(account_type=account_type,account_name=account_name,nfs_ipaddr=nfs_ipaddr,smb_name=smb_name,smb_passwd=smb_passwd)
        return JsonResponse (S2_SAN, status=200)

class S2DescribeAccounts(APIView):
    """
    get:
          获取NAS账号
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='s2_accounts', required=False, location='query', schema=coreschema.Anything ()),
            # coreapi.Field (name='account_types', required=False, location='query', description='', type='string'),
            # coreapi.Field (name='account_name', required=False, location='query', description='', type='string'),

        ]
    )
    @method_decorator (token_certify_decorator)
    def get(self, request):
        accounts = request.GET.get ('s2_accounts')
        s2_accounts = accounts.split ()
        S2_SAN = conn.describe_s2_accounts(s2_accounts=s2_accounts)#,account_types=account_types,account_name=account_name)
        return JsonResponse (S2_SAN, status=200)

class S2ModifyAccounts(APIView):
    """
    put:
          修改NAS账号信息
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='s2_account', required=True, location='query', type='string'),
            coreapi.Field (name='account_name', required=False, location='query', type='string'),
            coreapi.Field (name='description', required=False, location='query', type='string'),
        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request):
        s2_account = request.GET.get ('s2_account')
        account_name = request.GET.get('account_name')
        description = request.GET.get('description')
        S2_NAS = conn.modify_s2_account(s2_account=s2_account,account_name=account_name,description=description)
        return JsonResponse (S2_NAS)

class S2DeletAccount (APIView):
    """
    delete:
          删除NAS用户
    """
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            # coreapi.Field (name='s2_accounts', required=True, location='query', description='', type='string'),
        ]
    )
    @method_decorator (token_certify_decorator)
    def delete(self, request,s2_accounts):
        # s2_accounts = request.GET.get ('s2_accounts')
        s2_accounts = s2_accounts.split()
        S2 = conn.delete_s2_accounts(s2_accounts)
        return JsonResponse (S2)


class S2AssociateAccount (APIView):
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='account_id', required=True, location='form', schema=coreschema.Anything()),
            coreapi.Field (name='rw_flag', required=True, location='form', schema=coreschema.Anything()),
            coreapi.Field (name='s2_group', required=True, location='query', description='', type='string'),

        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request):
        s2_group = request.GET.get('s2_group')
        s2_accounts = json.loads (request.body)
        S2 = conn.associate_s2_account_group(s2_group=s2_group,s2_accounts=s2_accounts)
        return JsonResponse(S2)

class S2DissociateAccount (APIView):
    schema = AutoSchema (
        manual_fields=[
            coreapi.Field (name='Authorization', required=True, location='header', description='', type='string'),
            coreapi.Field (name='s2_groups', required=True, location='query', description='', type='string'),
            coreapi.Field (name='s2_accounts', required=True, location='query', description='', type='string'),

        ]
    )

    @method_decorator (token_certify_decorator)
    def put(self, request):
        # DocParam ("token")
        s2_groups = request.GET.get('s2_groups')
        s2_accounts = request.GET.get('s2_accounts')
        s2_accounts = s2_accounts.split()
        s2_groups = s2_groups.split()
        S2 = conn.dissociate_s2_account_group(s2_groups=s2_groups,s2_accounts=s2_accounts)
        return JsonResponse (S2)



# class S2(ViewSetMixin,APIView):
#     def retrieve(self, request,s2_id):
#         # S2_ID = json.loads (request.body)['ID']
#         S2_SAN = conn.describe_s2_servers(s2_servers=[s2_id])
#         return JsonResponse(S2_SAN, status=200)
#
#     def update(self, request,s2_id):
#         kw = json.loads (request.body)['container']
#         name = kw['name']
#         S2_SAN = conn.modify_s2_server([s2_id],name)
#         return JsonResponse(S2_SAN, status=200)
#
#     def update(self, request,s2_id):
#         body = json.loads (request.body)['container']
#         server_type = body['server_type']
#         S2_SAN = conn.resize_s2_servers([s2_id],server_type)
#         return JsonResponse(S2_SAN, status=200)




