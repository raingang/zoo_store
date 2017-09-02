from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.product_list, name = 'ProductList'),
               url(r'^category/(?P<category_slug>[-\w]+)/$', views.product_list, name = 'ProductListByCategory'),
               url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_detail, name = 'ProductDetail')
               ]