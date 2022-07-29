from django.contrib import admin

from .models import History

class HistoryAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content_type',
        'object_id',
        'content_object',
        'viewed_on'
    )

admin.site.register(History, HistoryAdmin)