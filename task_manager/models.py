from django.db import models
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self: 'Tag') -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self: 'Position') -> str:
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self: 'TaskType') -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        related_name='workers',
        null=True,
        on_delete=models.SET_NULL
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self: 'Worker') -> str:
        return self.username


class Task(models.Model):
    class Priority(models.TextChoices):
        URGENT = 'Urgent', 'urgent'
        HIGH = 'High', 'high'
        MEDIUM = 'Medium', 'medium'
        LOW = 'Low', 'low'

    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    task_type = models.ForeignKey(
        TaskType,
        related_name='tasks',
        on_delete=models.CASCADE
    )
    assignees = models.ManyToManyField(
        Worker,
        blank=True,
        related_name='tasks'
    )
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='tasks'
    )

    def __str__(self: 'Task') -> str:
        return self.name
