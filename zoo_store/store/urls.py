from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.product_list, name = 'ProductList'),
               url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name = 'ProductListByCategory')]