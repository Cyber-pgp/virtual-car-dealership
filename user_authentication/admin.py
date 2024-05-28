from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy as _
from django.urls import path

class MyAdminSite(AdminSite):
    site_header = _("My Admin")
    site_title = _("Admin Portal")
    index_title = _("Welcome to the Admin Portal")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # Add any custom URLs here
        ]
        return custom_urls + urls

admin_site = MyAdminSite(name='myadmin')

# Register your models with custom admin site
admin_site.register(YourModel)

class YourModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('css/custom_admin.css',)
        }
        js = ('js/custom_admin.js',)

# Register the customized admin site
admin_site.register(YourModel, YourModelAdmin)
