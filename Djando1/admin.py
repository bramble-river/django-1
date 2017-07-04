from django.contrib import admin

# Register your models here.
# from django.contrib import admin

from Djando1.models import UserInfo
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fields = ('user', 'pwd')
admin.site.register(UserInfo,ContactAdmin)
