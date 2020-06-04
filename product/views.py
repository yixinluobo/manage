from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from product import models, serializers
from util.response import APIResponse


class ProductAddAPIView(CreateAPIView):
    '''增加产品'''
    # 验证配置
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return APIResponse(results=response.data)


class ProductDelAPIView(DestroyAPIView):
    '''删除产品'''
    # 验证配置
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    # 重写删除方法
    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return APIResponse(data_msg='删除成功', results=response.data)


class ProductUpdateAPIView(UpdateAPIView):
    '''修改产品'''
    # 验证配置
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def put(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)


class ProductListAPIView(ListAPIView):
    '''查询产品'''
    # 验证配置
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    # 过滤配置
    filter_backends = [SearchFilter]
    search_fields = ['name', 'category']

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        return APIResponse(results=response.data)


class ProductUtilAPIView(RetrieveAPIView):
    # 验证配置
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        return APIResponse(results=response.data)


class OrderAddAPIView(CreateAPIView):
    '''添加账单'''
    # 验证配置
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return APIResponse(results=response.data)


class OrderDelAPIView(DestroyAPIView):
    '''删除账单'''
    # 验证配置
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return APIResponse(results=response.data)


class OrderQueryAPIView(ListAPIView):
    '''查询订单'''
    # 验证配置
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    # 过滤配置
    filter_backends = [OrderingFilter]
    ordering_fields = ['volumes']

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        return APIResponse(results=response.data)
