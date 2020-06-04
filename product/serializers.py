from rest_framework import serializers

from product import models


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(label='产品类型')

    class Meta:
        model = models.Product
        fields = ['id', 'name', 'code', 'category', 'category_name', 'price', 'stock', 'remarks']
        extra_kwargs = {
            'category': {
                'write_only': True
            }
        }

    def get_category_name(self, obj):
        category_num = obj.category
        if category_num == 0:
            return '精品'
        elif category_num == 1:
            return '轮胎'
        return '耗材'


class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField(label='产品名')
    total = serializers.SerializerMethodField(label='订单总金额')

    class Meta:
        model = models.Order
        fields = ['id', 'product', 'product_name', 'customer', 'phone', 'unit_price', 'volumes', 'total', 'remarks']
        extra_kwargs = {
            'product': {
                'write_only': True
            }
        }

    def get_product_name(self, obj):
        product_id = obj.product.pk
        product_name = models.Product.objects.get(pk=product_id).name
        return product_name

    def get_total(self, obj):
        unit_price = obj.unit_price
        volumes = obj.volumes
        total = unit_price * volumes
        return total
