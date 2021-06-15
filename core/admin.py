from django.contrib import admin
from core.models import Evento
from django.contrib.auth.models import User

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('id', 'titulo', 'data_evento',)


admin.site.register(Evento, EventoAdmin)
