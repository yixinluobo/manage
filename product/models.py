from django.db import models


class Product(models.Model):
    CATEGORY = [
        [0, '精品'],
        [1, '轮胎'],
        [2, '耗材']
    ]
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="产品名称")
    code = models.CharField(max_length=20, null=True, blank=True, verbose_name="产品代码")
    category = models.IntegerField(choices=CATEGORY, default=0)
    price = models.DecimalField('单价', max_digits=10, decimal_places=2)
    stock = models.IntegerField('库存', default=0)
    remarks = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')

    class Meta:
        db_table = 't_product'
        verbose_name = '产品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(to=Product,
                                on_delete=models.DO_NOTHING,
                                related_name="orders"
                                )
    customer = models.CharField(max_length=20, verbose_name='客户姓名')
    phone = models.CharField(max_length=11, verbose_name='客户手机')
    unit_price = models.DecimalField('销售单价', max_digits=10, decimal_places=2)
    volumes = models.IntegerField('销售数量')
    remarks = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')

    class Meta:
        db_table = 't_order'
        verbose_name = '账单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product.name
