from django.contrib.admin.sites import AdminSite
user_admin_site = AdminSite()

from django.contrib import admin

from fuzziverse.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    pass
user_admin_site.register(Application, ApplicationAdmin)
