from rest_framework.views import APIView
from user import models, serializers
from util.response import APIResponse


class LoginAPI(APIView):
    # 禁用登录认证
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # 前台账号用usr，密码用pwd
        user_ser = serializers.UserSerializer(data=request.data)
        try:
            user_ser.is_valid(raise_exception=True)
        except Exception as e:
            return APIResponse(data_status=1, data_msg='用户名或密码错误')
        return APIResponse(token=user_ser.token, results=serializers.UserSerializer(user_ser.user).data)





