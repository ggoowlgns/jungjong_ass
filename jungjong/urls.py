from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("product/put_product", views.put_product),
    path("product/update_product", views.update_product),
    path("yun/test", views.yun_test),
]
