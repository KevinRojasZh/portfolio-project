from django.contrib import admin
from .models import Developer, Lenguajes

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'direccion',
        'ciudad',
        'telefono',
        'email',
        'descripcion',
        'fotos',
        'created_by',
        
    ]
    filter_horizontal = ['tecnologias',]
    list_filter = ['tecnologias']

@admin.register(Lenguajes)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        
    ]
