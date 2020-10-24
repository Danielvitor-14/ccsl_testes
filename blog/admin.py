from django.contrib import admin
from .models import Post

@admin.register(Post)#?
class PostAdmin(admin.ModelAdmin): #?
    list_display   = ('titulo','autor','publicado','status') # Mostrar os campos destacados.

    list_filter    = ('status','criado','publicado','autor') # Lista de filtros para campos predefinidos.
    date_hierarchy = 'publicado' # Pesquisar por data os 'publlicados'
    raw_id_fields  = ('autor',) # Campo para adicionar o autor através de pesquisa. 
    search_fields  = ('titulo','conteudo')   # Colocar barra de pesquisa e filtra oq se pede.

    prepopulated_fields = {'slug':('titulo',)}  # Deixar o preenchimento do campo automatico através de outro campo.




# Register your models here.
