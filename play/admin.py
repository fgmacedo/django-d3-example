from django.contrib import admin


from .models import Play


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
