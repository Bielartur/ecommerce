from django.urls import path

from loja.views import homepage, loja, carrinho, checkout

urlpatterns = [
    path("", homepage, name="homepage"),
    path("loja/", loja, name="homepage"),
    path("carrinho/", carrinho, name="homepage"),
    path("checkout/", checkout, name="homepage"),
]