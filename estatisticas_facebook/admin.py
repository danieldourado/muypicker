from django.contrib import admin
from estatisticas_facebook.models import Page, PageInsights
from kindles.models import Modelo, Negociacao

# Register your models here.
admin.site.register(Page)
admin.site.register(Modelo)
admin.site.register(Negociacao)
admin.site.register(PageInsights)

