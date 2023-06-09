Certainly! Here's an updated README.md file with the pagination feature and the previous formatting:

```
# Task Manager RESTful API

This is a simple Task Manager RESTful API built using Python and Flask. The API allows you to manage tasks by performing CRUD (Create, Read, Update, Delete) operations.

## Requirements

- Python (3.11 or above)
- Flask
- Flask-PyMongo
```

## Getting Started

1. Clone this repository:

```
git clone <repository-url>
```

2. Change into the project directory:

 ```shell
   cd Task_Manager_API
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up the MongoDB connection:

   - Make sure you have MongoDB installed and running.
   - Update the MongoDB connection string in the `app.py` file:

```python
   client = MongoClient('mongodb://localhost:27017/')
```

4. Start the Flask server:

```
python app.py
```

The API server will start running at `http://localhost:5000`.

## API Endpoints

The following endpoints are available:

### Get all tasks

- **URL:** `/tasks`
- **Method:** `GET`
- **Query Parameters:**
  - `page`: The current page number (default: 1)
  - `limit`: The number of tasks per page (default: 10)

Retrieves all tasks with pagination support. The response includes the current page, limit, total tasks, total pages, and the tasks for the current page.

### Create a task

- **URL:** `/tasks`
- **Method:** `POST`
- **Request Body:**
  - `title`: The title of the task
  - `description`: The description of the task
  - `due_date`: The due date of the task (optional)
  - `status`: The status of the task (default: "Incomplete")

Creates a new task with the provided details and returns the created task.

### Get a task

- **URL:** `/tasks/<task_id>`
- **Method:** `GET`

Retrieves a single task by its ID.

### Update a task

- **URL:** `/tasks/<task_id>`
- **Method:** `PUT`
- **Request Body:** Any of the following attributes can be updated:
  - `title`: The new title of the task
  - `description`: The new description of the task
  - `due_date`: The new due date of the task
  - `status`: The new status of the task

Updates an existing task with the provided details and returns the updated task.

### Delete a task

- **URL:** `/tasks/<task_id>`
- **Method:** `DELETE`

Deletes a task by its ID.

## Pagination

The API supports pagination for the `/tasks` endpoint. You can include the following query parameters to control the pagination:

- `page`: The current page number (default: 1)
- `limit`: The number of tasks per page (default: 10)

For example, to retrieve the second page of tasks with 5 tasks per page, you can make a GET request to `/tasks?page=2&limit=5`.

The response will include the requested page of tasks along with information about the current page, limit, total tasks, and total pages.

## Error Handling

The API includes error handling for common scenarios. If a resource or endpoint is not found, the API will return an error response with the appropriate status code and error message.

- `404 Not Found`: When a requested resource or endpoint is not found.

## License

This project is licensed under the [MIT License](LICENSE).













