# membros/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo ao sistema de cadastro de membros!</h1>")
