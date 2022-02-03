from django.contrib import admin

from .models import (
    Usuario,
    Herramientas,
    Clasificacion,
    Unidades,
    Videos,
    Cursos
)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Herramientas)
admin.site.register(Clasificacion)

admin.site.register(Unidades)
admin.site.register(Videos)
admin.site.register(Cursos)