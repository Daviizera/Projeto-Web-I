from django.contrib import admin
from .models import Noticia  # Importe o seu modelo Noticia
from.models import Noticia, ConfiguracaoSite # 1. Importe o modelo ConfiguracaoSite
# Register your models here.

admin.site.register(Noticia)  # Registre o modelo Noticia no admin
admin.site.register(ConfiguracaoSite) # 2. Registre o modelo ConfiguracaoSite no admin