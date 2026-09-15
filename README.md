# task-tracker
# Task Tracker CLI

A simple command-line task tracker built with Python. Tasks are stored locally in a JSON file, making the project lightweight and easy to use without a database.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as `done`
- Mark tasks as `in-progress`
- List all tasks
- Filter tasks by status
- Automatically create `tasks.json` if it doesn't exist
- Store task creation and update timestamps
- Handle invalid task IDs and statuses

## Technologies Used

- Python 3
- JSON
- Python Standard Library
- `sys.argv` for command-line arguments
- `pathlib` for file handling
- `datetime` for timestamps

No external libraries or frameworks are required.

## Project Structure

```text
CLI_TASK/
├── task_cli.py
├── tasks.json
└── README.md