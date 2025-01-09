from django.contrib import admin
from .models import Developer

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'direccion',
        'ciudad',
        'telefono',
        'email',
        'descripcion',
        'tecnologias',
        'fotos',
        'created_by',
        
    ]
    list_filter = ['descripcion','tecnologias']
