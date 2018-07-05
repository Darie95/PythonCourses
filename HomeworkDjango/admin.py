from django.contrib import admin

from HomeworkDjango.models import Shop,Item,Department


class Shopsadmin(admin.ModelAdmin):
    list_display = ['id','name', 'staff_amount']

class Departmentsadmin(admin.ModelAdmin):
    list_display = ['id','sphere', 'staff_amount', 'shop']

class Itemsadmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'price', 'department', 'image']

admin.register(Shop, Item, Department)
admin.site.register(Shop, Shopsadmin)
admin.site.register(Item,Itemsadmin)
admin.site.register(Department, Departmentsadmin)
