# Task Manager CLI

## Project Overview
Simple CLI task management app demonstrating CRUD operations with priority levels and status tracking.

## Tech Stack
- Language: Python 3.8+
- Storage: JSON file-based
- Testing: pytest

## Project Structure
```
.
├── task_manager.py    # Core business logic (TaskManager, Task model)
├── storage.py         # JSON persistence layer
├── cli.py            # Command-line interface
└── requirements.txt   # Python dependencies
```

## Key Design Patterns
- **Repository Pattern**: `storage.py` abstracts data persistence
- **Service Layer**: `task_manager.py` contains business logic separate from UI
- **Dataclass**: Task model uses Python dataclass for immutability

## Commands
```bash
# Run application
python cli.py create "Title" "Description" [low|medium|high]
python cli.py list [priority_filter]
python cli.py update <task_id> [pending|in_progress|completed]
python cli.py delete <task_id>

# Testing
pytest                    # Run all tests
pytest --cov             # Run with coverage
pytest tests/test_*.py   # Run specific test file
```

## Code Style
IMPORTANT: Follow these conventions
- Use type hints for all function signatures
- Keep functions under 20 lines
- Use dataclasses for data models
- Named imports only (no `from x import *`)

## Development Guidelines
- **Adding new field to Task**: Update `Task` dataclass in `task_manager.py`, then update serialization in storage
- **Adding new filter**: Extend `list_tasks()` method in TaskManager class
- **Changing storage**: Modify only `storage.py` to maintain separation of concerns

## Testing Requirements
YOU MUST: Write tests for new features
- Test coverage: 80% minimum
- Use pytest fixtures for TaskManager setup
- Mock Storage layer in unit tests
- See `tests/` directory for examples (when created)

## Do Not
- DO NOT use print() in business logic (only in cli.py)
- DO NOT expose storage implementation details in TaskManager
- NEVER commit tasks.json to git (add to .gitignore)
