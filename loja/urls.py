from django.urls import path

from loja.views import homepage, loja, carrinho, checkout

urlpatterns = [
    path("", homepage, name="homepage"),
    path("loja/", loja, name="loja"),
    path("carrinho/", carrinho, name="carrinho"),
    path("checkout/", checkout, name="checkout"),
]