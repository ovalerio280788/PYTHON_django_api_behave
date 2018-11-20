from django.contrib import admin


# Register your models here.
from demo.models import Home, HomeSections, Articles


class CasasAdmin(admin.ModelAdmin):
    list_display = ['home_name', 'location']


admin.site.register(Home, CasasAdmin)


class SeccionesAdmin(admin.ModelAdmin):
    list_display = ['home', 'section_name']


admin.site.register(HomeSections, SeccionesAdmin)


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ['section', 'article_name', 'color', 'quantity', 'description']


admin.site.register(Articles, ArticulosAdmin)
