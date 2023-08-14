from django.contrib import admin
from django.http.request import HttpRequest

from apps.site_setup.models import MenuLink, SiteSetup


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path'
    search_fields = 'id', 'text', 'url_or_path'
    list_display_links = 'id',


class MenuLinksTabular(admin.TabularInline):
    model = MenuLink


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title',  'description'
    inlines = MenuLinksTabular,

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()
