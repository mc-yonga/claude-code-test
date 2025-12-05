import pytest
from unittest.mock import Mock
from task_manager import TaskManager, Task
from storage import Storage


@pytest.fixture
def mock_storage():
    storage = Mock(spec=Storage)
    storage.load.return_value = []
    return storage


@pytest.fixture
def task_manager(mock_storage):
    return TaskManager(mock_storage)


@pytest.fixture
def task_manager_with_tasks(mock_storage):
    mock_storage.load.return_value = [
        {
            'id': 1,
            'title': 'Test Task 1',
            'description': 'Description 1',
            'priority': 'high',
            'status': 'pending',
            'created_at': '2025-01-01T10:00:00',
            'due_date': '2025-12-31'
        },
        {
            'id': 2,
            'title': 'Test Task 2',
            'description': 'Description 2',
            'priority': 'low',
            'status': 'completed',
            'created_at': '2025-01-02T10:00:00',
            'due_date': None
        }
    ]
    return TaskManager(mock_storage)


class TestCreateTask:
    def test_create_task_basic(self, task_manager, mock_storage):
        task = task_manager.create_task('New Task', 'Task description', 'medium')

        assert task.id == 1
        assert task.title == 'New Task'
        assert task.description == 'Task description'
        assert task.priority == 'medium'
        assert task.status == 'pending'
        assert task.created_at is not None
        assert task.due_date is None
        mock_storage.save.assert_called_once()

    def test_create_task_with_due_date(self, task_manager, mock_storage):
        task = task_manager.create_task('Task', 'Desc', 'high', '2025-12-31')

        assert task.due_date == '2025-12-31'
        mock_storage.save.assert_called_once()

    def test_create_task_auto_increment_id(self, task_manager_with_tasks, mock_storage):
        task = task_manager_with_tasks.create_task('New Task', 'Desc', 'low')

        assert task.id == 3

    def test_create_task_saves_to_storage(self, task_manager, mock_storage):
        task_manager.create_task('Task', 'Desc', 'high')

        mock_storage.save.assert_called_once()
        saved_tasks = mock_storage.save.call_args[0][0]
        assert len(saved_tasks) == 1
        assert saved_tasks[0]['title'] == 'Task'


class TestListTasks:
    def test_list_all_tasks(self, task_manager_with_tasks):
        tasks = task_manager_with_tasks.list_tasks()

        assert len(tasks) == 2
        assert tasks[0]['title'] == 'Test Task 1'
        assert tasks[1]['title'] == 'Test Task 2'

    def test_list_tasks_empty(self, task_manager):
        tasks = task_manager.list_tasks()

        assert tasks == []

    def test_list_tasks_filter_by_priority(self, task_manager_with_tasks):
        tasks = task_manager_with_tasks.list_tasks(priority_filter='high')

        assert len(tasks) == 1
        assert tasks[0]['priority'] == 'high'
        assert tasks[0]['title'] == 'Test Task 1'

    def test_list_tasks_filter_no_match(self, task_manager_with_tasks):
        tasks = task_manager_with_tasks.list_tasks(priority_filter='medium')

        assert tasks == []

    def test_list_tasks_preserves_all_fields(self, task_manager_with_tasks):
        tasks = task_manager_with_tasks.list_tasks()

        first_task = tasks[0]
        assert 'id' in first_task
        assert 'title' in first_task
        assert 'description' in first_task
        assert 'priority' in first_task
        assert 'status' in first_task
        assert 'created_at' in first_task
        assert 'due_date' in first_task
