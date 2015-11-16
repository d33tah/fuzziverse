# #Uncomment this to test issue #1:
#from fuzziverse.user_admin import user_admin_site
from django.contrib.admin import AdminSite
user_admin_site = AdminSite()

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from fuzziverse import models
class FileUploadInline(NestedStackedInline):
    model = models.InputTestCase
    min_num = 1
    extra = 0

class ReportInline(NestedStackedInline):
    model = models.Report
    min_num = 1
    extra = 0

class FuzzingAttemptInline(NestedStackedInline):
    model = models.FuzzingAttempt
    min_num = 1
    extra = 0
    inlines = [FileUploadInline]
    readonly_fields = ['created']

class ApplicationAdmin(NestedModelAdmin):
    inlines = [ReportInline, FuzzingAttemptInline]
user_admin_site.register(models.Application, ApplicationAdmin)
