from mock import patch, call
from django_nameko import rpc, get_pool, destroy_pool
# from nose import tools
from six.moves import queue as queue_six
from django.test.utils import override_settings
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


settings.configure()

@override_settings(NAMEKO_CONFIG=dict(AMQP_URL='amqp://'))
def test_get_pool():
    with patch('django_nameko.rpc.ClusterRpcProxy') as FakeClusterRpcProxy:
        pool = get_pool()
        with pool.next() as client:
            client.foo.bar()
            assert call().start().foo.bar() in FakeClusterRpcProxy.mock_calls
        destroy_pool()