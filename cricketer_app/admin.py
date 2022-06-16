from django.contrib import admin
from . models import Cricketer, Role, Type

# Register your models here.

admin.site.register(Cricketer)
admin.site.register(Role)
admin.site.register(Type)