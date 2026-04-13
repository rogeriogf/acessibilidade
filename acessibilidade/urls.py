from django.contrib import admin
from django.urls import path
from leituras.views import listar_acessos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_acessos),
]