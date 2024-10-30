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
    TaskFilterForm,
    WorkerFilterForm
)

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'task_manager/task/task_list.html'
    paginate_by = settings.PAGINATION_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = TaskSearchForm()
        context["filter_form"] = TaskFilterForm(prefix="filter")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
<<<<<<< HEAD
            queryset = queryset.filter(name__icontains=form.cleaned_data['name'])
        return queryset
=======
            name = form.cleaned_data.get('name')
            if name:
                queryset = queryset.filter(name__icontains=name)

            position = form.cleaned_data.get('position')
            if position:
                queryset = queryset.filter(worker__position=position)

            is_completed = form.cleaned_data.get('is_completed')
            if is_completed is not None:
                queryset = queryset.filter(is_completed=is_completed)

            phone_number = form.cleaned_data.get('phone_number')
            if phone_number:
                queryset = queryset.filter(phone_number__icontains=phone_number)

        return queryset

>>>>>>> f2919bdf2b8d1f371c877cb7c19922a4b1a32fc5

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

<<<<<<< HEAD
    def get_context_data(self, *, object_list=None, **kwargs):
=======
    def get_context_data(self, **kwargs):
>>>>>>> f2919bdf2b8d1f371c877cb7c19922a4b1a32fc5
        context = super().get_context_data(**kwargs)
        context['search_form'] = WorkerSearchForm()
        context['filter_form'] = WorkerFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = WorkerFilterForm(self.request.GET)

        if filter_form.is_valid():
            name = filter_form.cleaned_data.get('name')
            if name:
                queryset = queryset.filter(username__icontains=name)

            phone_number = filter_form.cleaned_data.get('phone_number')
            position = filter_form.cleaned_data.get('position')

            if position:
                queryset = queryset.filter(position=position)

            if phone_number:
                queryset = queryset.filter(phone_number__icontains=phone_number)

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

def logged_out(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('logged_out_page')

@login_required
def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    completed_tasks = Task.objects.filter(assignees=worker, is_completed=True)
    incomplete_tasks = Task.objects.filter(assignees=worker, is_completed=False)

    return render(request, 'task_manager/worker/worker_detail.html', {
        'worker': worker,
        'completed_tasks': completed_tasks,
        'incomplete_tasks': incomplete_tasks,
    })

@login_required
def add_task_to_worker(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.assignees.add(request.user)
    return redirect('task_manager:task-detail', pk=task.id)

@login_required
def remove_task_from_worker(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.assignees.remove(request.user)
    return redirect('task_manager:task-detail', pk=task.id)

@login_required
def home_page(request):
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()

    context = {
        'num_tasks': num_tasks,
        'num_workers': num_workers,
    }

    return render(request, 'task_manager/home_page.html', context)

@login_required
def my_task_manager(request):
    my_tasks = Task.objects.filter(assignees=request.user)
    return render(request, 'task_manager/task/my_task_manager.html', {'my_tasks': my_tasks})
