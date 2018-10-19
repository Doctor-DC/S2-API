from rest_framework import serializers
from snippets.models import Snippets


class S2Serializer(serializers.ModelSerializer):
    # token = serializers.CharField (label='登录状态token', read_only=True)  # 增加token字段
    class Meta:
        model = Snippets
        fields = '__all__'
        # fields = ('id', 'song', 'singer','token', 'last_modify_date', 'created')
