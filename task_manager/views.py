from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from task_manager.models import Task, Worker
from task_manager.forms import (
    TaskForm,
    WorkerSearchForm,
    TaskSearchForm,
    TaskUpdateForm,
    WorkerUpdateForm,
    WorkerForm,
)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'task_manager/task/task_list.html'
    paginate_by = settings.PAGINATION_SIZE

    def get_context_data(
            self: 'TaskListView',
            *,
            object_list: list = None,
            **kwargs: dict
    ) -> dict:
        context = super().get_context_data(**kwargs)
        context['search_form'] = TaskSearchForm()
        return context

    def get_queryset(self: 'TaskListView') -> list:
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return self.model.objects.filter(
                name__icontains=form.cleaned_data['name']
            )
        return self.model.objects.all()


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_manager/task/task_detail.html'


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    context_object_name = 'task'
    success_url = reverse_lazy('task_manager:task-list')
    template_name = 'task_manager/task/task_form.html'


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    context_object_name = 'task'
    form_class = TaskUpdateForm
    template_name = 'task_manager/task/task_form.html'
    success_url = reverse_lazy('task_manager:task-list')


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_manager:task-list')


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = 'worker_list'
    template_name = 'task_manager/worker/worker_list.html'
    paginate_by = settings.PAGINATION_SIZE

    def get_context_data(
            self: 'WorkerListView',
            *,
            object_list: list = None,
            **kwargs: dict
    ) -> dict:
        context = super().get_context_data(**kwargs)
        context['search_form'] = WorkerSearchForm()
        return context

    def get_queryset(self: 'WorkerListView') -> list:
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(username__icontains=name)
        return queryset


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy('task_manager:worker-list')
    template_name = 'task_manager/worker/worker_form.html'


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    success_url = reverse_lazy('task_manager:worker-list')
    form_class = WorkerUpdateForm
    template_name = 'task_manager/worker/worker_form.html'


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    context_object_name = 'worker'
    success_url = reverse_lazy('task_manager:worker-list')


class LoggedOutView(TemplateView):
    template_name = 'registration/logged_out.html'


def logged_out(request: HttpRequest) -> redirect:
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('logged_out_page')


@login_required
def worker_detail(request: HttpRequest, pk: int) -> render:
    worker = get_object_or_404(Worker, pk=pk)
    completed_tasks = Task.objects.filter(
        assignees=worker,
        is_completed=True
    )
    incomplete_tasks = Task.objects.filter(
        assignees=worker,
        is_completed=False
    )

    return render(
        request,
        'task_manager/worker/worker_detail.html',
        {
            'worker': worker,
            'completed_tasks': completed_tasks,
            'incomplete_tasks': incomplete_tasks,
        },
    )


@login_required
def add_task_to_worker(request: HttpRequest, task_id: int) -> redirect:
    task = get_object_or_404(Task, id=task_id)
    task.assignees.add(request.user)
    return redirect('task_manager:task-detail', pk=task.id)


@login_required
def remove_task_from_worker(request: HttpRequest, task_id: int) -> redirect:
    task = get_object_or_404(Task, id=task_id)
    task.assignees.remove(request.user)
    return redirect('task_manager:task-detail', pk=task.id)


@login_required
def home_page(request: HttpRequest) -> render:
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()

    context = {
        'num_tasks': num_tasks,
        'num_workers': num_workers,
    }

    return render(request, 'task_manager/home_page.html', context)
