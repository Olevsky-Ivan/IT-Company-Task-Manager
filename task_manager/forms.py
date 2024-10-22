from django import forms
from task_manager.models import Worker, Task
from django.contrib.auth.forms import UserCreationForm


class WorkerForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'position'
        ]


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'position'
        ]


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'deadline',
            'priority',
            'task_type',
            'assignees',
        ]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'deadline',
            'priority',
            'task_type',
            'assignees',
            'tag',
            'is_completed',
        ]


class WorkerSearchForm(forms.Form):
    name = forms.CharField(max_length=200, label='Search by name')


class TaskSearchForm(forms.Form):
    name = forms.CharField(max_length=200, label='Search by name')
