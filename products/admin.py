from django.contrib import admin
from .models import Computers , Test

class ProductAdmin(admin.ModelAdmin):
    list_display = ['make','price','category','active']
    list_editable = ['category','active']
    search_fields = ['make']

admin.site.register(Computers,ProductAdmin)
admin.site.register(Test)
