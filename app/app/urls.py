from django.urls import path
from membros.views import home  # A importação correta
from django.contrib import admin

urlpatterns = [
    path('', home, name='home'),  # A URL que chamará a função home
        path('admin/', admin.site.urls),  # Rota do painel de administração

]
