from django.db import models

class Noticia(models.Model):
    titulo_lista = models.CharField(
    max_length=200,
    blank=True,
    null=True,
    help_text="Título que aparecerá na lista de notícias"
    )

    titulo_detalhe = models.CharField(
    max_length=200,
    blank=True,
    null=True,
    help_text="Título que aparecerá dentro da notícia"
    )

    subtitulo = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        help_text="Subtítulo exibido na página de detalhe"
    )
    conteudo = models.TextField()  # Texto principal da notícia
    imagem = models.ImageField(
        upload_to='noticias_imagens/',
        blank=True,
        null=True,
        help_text="Imagem exibida apenas no detalhe"
    )
    link = models.URLField(blank=True, null=True, help_text="Link externo para a notícia completa")
    categoria = models.CharField(max_length=50, blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.titulo_lista:
            return self.titulo_lista
        elif self.titulo_detalhe:
            return self.titulo_detalhe
        else:
            return f"Notícia {self.id}"


class ConfiguracaoSite(models.Model):
    banner = models.ImageField(
        upload_to='site/',
        help_text="O banner principal que aparecerá no topo de todas as páginas."
    )

    def save(self, args, **kwargs):
        self.pk = 1
        super().save(args, **kwargs)

    def str(self):
        return "Configuração do Site"