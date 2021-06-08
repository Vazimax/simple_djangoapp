from django.contrib import admin
from .models import *

class AppAdmin(admin.ModelAdmin):
    pass

admin.site.register(Login)
admin.site.site_header = 'YOMAX'
admin.site.site_title = 'YOMAX'
