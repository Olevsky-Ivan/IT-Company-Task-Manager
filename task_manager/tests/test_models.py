from django.test import TestCase
from django.utils import timezone
from task_manager.models import Tag, Position, TaskType, Worker, Task


class TagModelTest(TestCase):
    def setUp(self: 'TagModelTest') -> None:
        self.tag = Tag.objects.create(name='Urgent')

    def test_tag_creation(self: 'TagModelTest') -> None:
        self.assertEqual(self.tag.name, 'Urgent')

    def test_tag_str(self: 'TagModelTest') -> None:
        self.assertEqual(str(self.tag), 'Urgent')


class PositionModelTest(TestCase):
    def setUp(self: 'PositionModelTest') -> None:
        self.position = Position.objects.create(name='Developer')

    def test_position_creation(self: 'PositionModelTest') -> None:
        self.assertEqual(self.position.name, 'Developer')

    def test_position_str(self: 'PositionModelTest') -> None:
        self.assertEqual(str(self.position), 'Developer')


class TaskTypeModelTest(TestCase):
    def setUp(self: 'TaskTypeModelTest') -> None:
        self.task_type = TaskType.objects.create(name='Bug Fix')

    def test_task_type_creation(self: 'TaskTypeModelTest') -> None:
        self.assertEqual(self.task_type.name, 'Bug Fix')

    def test_task_type_str(self: 'TaskTypeModelTest') -> None:
        self.assertEqual(str(self.task_type), 'Bug Fix')


class WorkerModelTest(TestCase):
    def setUp(self: 'WorkerModelTest') -> None:
        self.position = Position.objects.create(name='Tester')
        self.worker = Worker.objects.create_user(
            username='john_doe',
            password='password123',
            position=self.position,
            phone_number='1234567890'
        )

    def test_worker_creation(self: 'WorkerModelTest') -> None:
        self.assertEqual(self.worker.username, 'john_doe')
        self.assertEqual(self.worker.phone_number, '1234567890')
        self.assertEqual(self.worker.position, self.position)

    def test_worker_str(self: 'WorkerModelTest') -> None:
        self.assertEqual(str(self.worker), 'john_doe')


class TaskModelTest(TestCase):
    def setUp(self: 'TaskModelTest') -> None:
        self.task_type = TaskType.objects.create(name='Development')
        self.worker = Worker.objects.create_user(
            username='jane_doe',
            password='password123'
        )
        self.tag = Tag.objects.create(name='Important')
        self.task = Task.objects.create(
            name='Create Django Tests',
            description='Write unit tests for Django models and admin.',
            deadline=timezone.now() + timezone.timedelta(days=7),
            priority=Task.Priority.HIGH,
            task_type=self.task_type
        )
        self.task.assignees.add(self.worker)
        self.task.tag.add(self.tag)

    def test_task_creation(self: 'TaskModelTest') -> None:
        self.assertEqual(self.task.name, 'Create Django Tests')
        self.assertEqual(self.task.priority, Task.Priority.HIGH)
        self.assertIn(self.worker, self.task.assignees.all())
        self.assertIn(self.tag, self.task.tag.all())

    def test_task_str(self: 'TaskModelTest') -> None:
        self.assertEqual(str(self.task), 'Create Django Tests')
