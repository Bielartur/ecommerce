from django.shortcuts import render

# Create your views here.
def minha_conta(request):
    return render(request, "minhaconta.html")

def login(request):
    return render(request, "login.html")