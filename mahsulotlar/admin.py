from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Customer)
admin.site.register(Product)

from django.contrib import admin
from .models import ElektronXizmat

@admin.register(ElektronXizmat)
class ElektronXizmatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'narx', 'rasm')
