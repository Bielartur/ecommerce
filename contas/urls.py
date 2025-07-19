from django.urls import path

from contas.views import minha_conta, login

urlpatterns = [
    path("minhaconta/", minha_conta, name="minha_conta"),
    path("login/", login, name="login"),
]