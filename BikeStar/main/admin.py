from django.contrib import admin
from .models import Route

# Register your models here.
class RouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 
                    'created_date', 'updated_date', 'get_html_image']
   

admin.site.register(Route, RouteAdmin)