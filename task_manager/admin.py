from django.contrib import admin

from task_manager.models import Tag, Position, TaskType, Worker, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('username', 'position', 'phone_number', 'email')
    search_fields = ('username', 'email', 'position__name')
    list_filter = ('position',)
    autocomplete_fields = ['position']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'task_type',
        'deadline',
        'is_completed',
        'priority'
    )
    search_fields = ('name', 'task_type__name')
    list_filter = ('is_completed', 'priority', 'deadline', 'task_type')
    autocomplete_fields = ['task_type', 'assignees', 'tag']
    filter_horizontal = ('assignees', 'tag')
