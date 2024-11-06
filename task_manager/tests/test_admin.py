from django.contrib.admin.sites import site
from django.test import TestCase
from task_manager.models import Tag, Position, TaskType, Worker, Task


class AdminSiteTests(TestCase):
    def test_tag_in_admin(self: 'AdminSiteTests') -> None:
        self.assertIn(Tag, site._registry)

    def test_position_in_admin(self: 'AdminSiteTests') -> None:
        self.assertIn(Position, site._registry)

    def test_task_type_in_admin(self: 'AdminSiteTests') -> None:
        self.assertIn(TaskType, site._registry)

    def test_worker_in_admin(self: 'AdminSiteTests') -> None:
        self.assertIn(Worker, site._registry)

    def test_task_in_admin(self: 'AdminSiteTests') -> None:
        self.assertIn(Task, site._registry)
