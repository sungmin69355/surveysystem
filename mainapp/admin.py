from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import AccountsModel
# Register your models here.

class AccountsModelAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(AccountsModel, AccountsModelAdmin)