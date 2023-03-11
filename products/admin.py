from django.contrib import admin
from products.models import Version


class VersionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "software",
        "version"
    ]


admin.site.register(Version, VersionAdmin)
