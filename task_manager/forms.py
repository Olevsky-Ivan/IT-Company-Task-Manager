from django import forms
from task_manager.models import Worker, Task, TaskType
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
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=True
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline', 'priority', 'task_type', 'assignees']

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


class TaskFilterForm(forms.Form):
    is_completed = forms.BooleanField(
        required=False,
        label="Completed Tasks",
    )
    task_type = forms.ModelChoiceField(
        required=False,
        queryset=TaskType.objects.all(),
        label="Task Type",
        empty_label="Any Task Type"
    )


class WorkerFilterForm(forms.Form):
    phone_number = forms.ModelChoiceField(
        required=False,
        queryset=Worker.objects.all(),
        label="Phone Number",
        empty_label="Any Phone Number"
    )
    position = forms.ModelChoiceField(
        required=False,
        queryset=Worker.objects.all(),
        label="Position",
        empty_label="Any Position"
    )
