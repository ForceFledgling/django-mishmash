from apps.wiki.models import Category, Page

from django.contrib import admin


class PageAdmin(admin.ModelAdmin):
    list_filter = (['category'])
    # exclude = ['date_publish', 'date_edit']
    readonly_fields = ['date_publish', 'date_edit']


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
