from django.shortcuts import render
from .models import Noticia # Importa o nosso modelo de dados
from django.shortcuts import render, get_object_or_404
# Create your views here.

def lista_noticias(request):
    # Busca todos os objetos Noticia no banco de dados, ordenando pelos mais recentes
    todas_as_noticias = Noticia.objects.all().order_by('-data_publicacao')
    
    #Prepara o "contexto" que será enviado para o template.
    #A chave 'noticias' será o nome que usaremos no HTML para acessar os dados.
    contexto = {'noticias': todas_as_noticias}

    #Renderiza o template HTML, passando o request e o contexto.
    return render(request, 'noticias/lista_noticias.html', contexto)


def lista_noticias(request):
    todas_as_noticias = Noticia.objects.all().order_by('-data_publicacao')
    contexto = {'noticias': todas_as_noticias}
    return render(request, 'noticias/lista_noticias.html', contexto)

def detalhe_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    contexto = {'noticia': noticia}
    return render(request, 'noticias/detalhe_noticia.html', contexto)
