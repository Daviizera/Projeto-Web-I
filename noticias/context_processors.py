from .models import ConfiguracaoSite

def site_config(request):
    try:
        config = ConfiguracaoSite.objects.get(pk=1)
        return {'site_config': config}
    except ConfiguracaoSite.DoesNotExist:
        return {'site_config': None}