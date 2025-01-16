from django.contrib import admin
from django.utils import timezone
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('due_date',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_at = timezone.now()
        obj.updated_at = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.register(Task, TaskAdmin)
