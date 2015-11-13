from django.contrib import admin

from .models import Bundle, Link, BundleLink


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', )


@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    list_display = ('title', 'at', )


@admin.register(BundleLink)
class BundleLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'bundle', 'curator', 'comfort_level', )
    select_related = True
