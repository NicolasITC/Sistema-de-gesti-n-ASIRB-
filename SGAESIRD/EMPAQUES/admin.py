from django.contrib import admin
from .models import Usuario, Categoria_anotaciones, Anotaciones, Turnos, Finanzas, Anuncios, Comentarios, Universidades, Lista_de_Espera, Toma_turnos, Mensaje_inicio

# Register your models here.

	
admin.site.register(Toma_turnos)
admin.site.register(Usuario)
admin.site.register(Categoria_anotaciones)
admin.site.register(Anotaciones)
admin.site.register(Turnos)
admin.site.register(Finanzas)
admin.site.register(Anuncios)
admin.site.register(Comentarios)
admin.site.register(Universidades)
admin.site.register(Lista_de_Espera)
admin.site.register(Mensaje_inicio)