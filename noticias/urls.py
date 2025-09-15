from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_noticias, name='lista_noticias'),
    path('noticia/<int:noticia_id>/', views.detalhe_noticia, name='detalhe_noticia'),
]

