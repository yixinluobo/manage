from django.conf.urls import url

from product import views

urlpatterns = [
    # 产品
    url(r'^add-product/$', views.ProductAddAPIView.as_view()),
    url(r'^del-product/(?P<pk>.*)/$', views.ProductDelAPIView.as_view()),
    url(r'^update-product/(?P<pk>.*)/$', views.ProductUpdateAPIView.as_view()),
    url(r'^query-product/$', views.ProductListAPIView.as_view()),
    url(r'^query-product/(?P<pk>.*)/$', views.ProductUtilAPIView.as_view()),
    # 订单
    url(r'^add-order/$', views.OrderAddAPIView.as_view()),
    url(r'^del-order/(?P<pk>.*)/$', views.OrderDelAPIView.as_view()),
    url(r'^query-order/$', views.OrderQueryAPIView.as_view()),
]