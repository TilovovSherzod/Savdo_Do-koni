from django.contrib import admin
from .models import ElektronXizmat

@admin.register(ElektronXizmat)
class ElektronXizmatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'narx', 'rasm')
