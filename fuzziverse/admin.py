from fuzziverse.user_admin import user_admin_site

from django.contrib import admin

from fuzziverse.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    pass
user_admin_site.register(Application, ApplicationAdmin)
