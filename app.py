from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')  
db = client['task_manager']
tasks_collection = db['tasks']

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Routes
# Get All Task
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    total_tasks = tasks_collection.count_documents({})
    total_pages = (total_tasks + limit - 1) // limit

    if page > total_pages:
        return jsonify({"error": "Page not found"}), 404

    skip = (page - 1) * limit
    tasks = list(tasks_collection.find().skip(skip).limit(limit))
    for task in tasks:
        task['_id'] = str(task['_id'])

    response = {
        "page": page,
        "limit": limit,
        "total_tasks": total_tasks,
        "total_pages": total_pages,
        "tasks": tasks
    }
    return jsonify(response)

# Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('due_date')
    status = data.get('status', 'Incomplete')

    task = {
        'title': title, 
        'description': description,
        'due_date': due_date,
        'status': status
    }

    result = tasks_collection.insert_one(task)
    task['_id'] = str(result.inserted_id)
    return jsonify(task), 201

# Get Task
@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})
    if task:
        task['_id'] = str(task['_id'])
        return jsonify(task)
    else:
        return jsonify({"error": "Task not found"}), 404

# Update Task
@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    updated_task = {
        'title': data.get('title', task['title']),
        'description': data.get('description', task['description']),
        'due_date': data.get('due_date', task['due_date']),
        'status': data.get('status', task['status'])
    }

    result = tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': updated_task})
    if result.modified_count:
        updated_task['_id'] = task_id
        return jsonify(updated_task)
    else:
        return jsonify({"error": "Task not found"}), 404

# Delete Task
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    deleted_task = tasks_collection.find_one_and_delete({'_id': ObjectId(task_id)})
    
    if deleted_task:
        deleted_task['_id'] = str(deleted_task['_id'])
        return jsonify({"message": "Task deleted","Deleted Task":deleted_task})
    else:
        return jsonify({"error": "Task not found"}), 404


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
