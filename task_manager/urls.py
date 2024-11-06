from django.urls import path
from task_manager.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    WorkerListView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    add_task_to_worker,
    remove_task_from_worker,
    worker_detail,
    home_page,
    my_task_manager
)

app_name = 'task_manager'

urlpatterns = [
    path('my_task/', my_task_manager, name='my-tasks'),
    path('task/', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path(
        'task/<int:pk>/delete/',
        TaskDeleteView.as_view(),
        name='task-delete'
    ),
    path(
        'task/<int:pk>/update/',
        TaskUpdateView.as_view(),
        name='task-update'
    ),

    path('worker/', WorkerListView.as_view(), name='worker-list'),
    path('worker/<int:pk>/', worker_detail, name='worker-detail'),
    path('worker/create/', WorkerCreateView.as_view(), name='worker-create'),
    path(
        'worker/<int:pk>/delete/',
        WorkerDeleteView.as_view(),
        name='worker-delete'
    ),
    path(
        'worker/<int:pk>/update/',
        WorkerUpdateView.as_view(),
        name='worker-update'
    ),

    path('task/<int:task_id>/add/', add_task_to_worker,
         name='add_task_to_worker'),
    path('task/<int:task_id>/remove/', remove_task_from_worker,
         name='remove_task_from_worker'),
    path('', home_page, name='home_page'),
]
