import re

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from user import models

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    usr = serializers.CharField(write_only=True)
    pwd = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['usr', 'pwd', 'username', 'email']
        extra_kwargs = {
            'username': {
                'read_only': True
            },
            'email': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        usr = attrs.get('usr')
        pwd = attrs.get('pwd')

        if re.match(r'.+@.+', usr):
            user_query = models.User.objects.filter(email=usr)
        elif re.match(r'1[3-9][0-9]{9}', usr):
            user_query = models.User.objects.filter(mobile=usr)
        else:
            user_query = models.User.objects.filter(username=usr)

        user = user_query.first()
        if user and user.check_password(pwd):
            # 签发token, 将token存放到实例化类对象的token名字中
            payload = jwt_payload_handler(user)
            self.token = jwt_encode_handler(payload)
            self.user = user
            return attrs

        raise serializers.ValidationError({'data': '数据有误'})
