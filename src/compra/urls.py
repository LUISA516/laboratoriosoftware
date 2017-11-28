from django.conf.urls import url, include
from compra.views import indexCompra, compra_view



urlpatterns = [
url(r'^$', indexCompra),
url(r'^compras$', compra_view, name='index_compra'),
]