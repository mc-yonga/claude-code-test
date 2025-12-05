from dataclasses import dataclass, asdict
from typing import List, Optional
from datetime import datetime
from storage import Storage


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: str
    status: str
    created_at: str
    due_date: Optional[str] = None


class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def create_task(self, title: str, description: str, priority: str, due_date: Optional[str] = None) -> Task:
        task_id = max([t['id'] for t in self.tasks], default=0) + 1
        task = Task(
            id=task_id,
            title=title,
            description=description,
            priority=priority,
            status='pending',
            created_at=datetime.now().isoformat(),
            due_date=due_date
        )
        self.tasks.append(asdict(task))
        self.storage.save(self.tasks)
        return task

    def list_tasks(self, priority_filter: Optional[str] = None) -> List[dict]:
        if priority_filter:
            return [t for t in self.tasks if t['priority'] == priority_filter]
        return self.tasks

    def update_status(self, task_id: int, status: str) -> bool:
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = status
                self.storage.save(self.tasks)
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        original_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        if len(self.tasks) < original_length:
            self.storage.save(self.tasks)
            return True
        return False
