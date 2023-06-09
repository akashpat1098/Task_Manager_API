# Task Manager API

This is a RESTful API for managing tasks.

## Setup

1. Clone the repository:

      git clone <repository-url>


2. Install the dependencies:

      pip install -r requirements.txt 

3. Run the application:

      python app.py
## Endpoints

- `GET /tasks`: Get all tasks.
- `POST /tasks`: Create a new task.
- `GET /tasks/<task_id>`: Get a single task by its ID.
- `PUT /tasks/<task_id>`: Update an existing task.
- `DELETE /tasks/<task_id>`: Delete a task.

## Task Object

The task object has the following properties:

- ID (auto-generated and unique)
- Title
- Description
- Due Date
- Status (can be "Incomplete", "In Progress", or "Completed")
