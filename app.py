
# from flask import Flask, request, jsonify
# from flask_migrate import Migrate
# from pydantic import ValidationError
# from models import db, Task
# from schemas import TaskCreate, TaskUpdate, TaskList

# app = Flask(__name__)
# app.config.from_object('config.Config')
# db.init_app(app)
# migrate = Migrate(app, db)

# @app.before_request
# def create_tables():
#     db.create_all()

# # Create a new task
# @app.route('/')
# def index():
#     return "Welcome to the Task Manager API"



# @app.before_request
# def create_tables():
#     db.create_all()



# # Unify single and bulk task creation
# @app.route('/v1/tasks', methods=['POST'])
# def bulk_add_tasks():
#     data = request.get_json()
#     tasks_data = data.get("tasks", [])
    
#     tasks = []
#     validation_errors = []
    
#     for index, task_data in enumerate(tasks_data):
#         try:
#             validated_task_data = TaskCreate(**task_data)
#             task = Task(title=validated_task_data.title, is_completed=validated_task_data.is_completed)
#             tasks.append(task)
#         except ValidationError as e:
#             validation_errors.append({
#                 "index": index,
#                 "errors": e.errors(),
#                 "input": task_data
#             })
    
#     if validation_errors:
#         return jsonify(errors=validation_errors), 400

#     # Bulk save tasks and commit
#     db.session.bulk_save_objects(tasks)
#     db.session.commit()
    
#     # Return the IDs of the newly created tasks
#     return jsonify(tasks=[{"id": task.id} for task in tasks]), 201




# # List all tasks
# @app.route('/v1/tasks', methods=['GET'])
# def list_tasks():
#     tasks = Task.query.all()
#     return TaskList(tasks=[task.to_dict() for task in tasks]).json(), 200

# # Get a specific task
# @app.route('/v1/tasks/<int:id>', methods=['GET'])
# def get_task(id):
#     task = Task.query.get_or_404(id)
#     return task.to_dict(), 200

# # Delete a specific task
# @app.route('/v1/tasks/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     task = Task.query.get_or_404(id)
#     db.session.delete(task)
#     db.session.commit()
#     return '', 204

# # Edit a specific task
# @app.route('/v1/tasks/<int:id>', methods=['PUT'])
# def update_task(id):
#     task = Task.query.get_or_404(id)
#     data = request.get_json()
#     try:
#         task_data = TaskUpdate(**data)
#     except ValidationError as e:
#         return jsonify(errors=e.errors()), 400

#     task.title = task_data.title
#     task.is_completed = task_data.is_completed
#     db.session.commit()
#     return '', 204


# @app.route('/v1/tasks', methods=['DELETE'])
# def bulk_delete_tasks():
#     data = request.get_json()
#     ids = [task["id"] for task in data.get("tasks", [])]
#     Task.query.filter(Task.id.in_(ids)).delete(synchronize_session=False)
#     db.session.commit()
#     return '', 204

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from pydantic import ValidationError
from models import db, Task
from schemas import TaskCreate, TaskUpdate, TaskList

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
migrate = Migrate(app, db)

@app.before_request
def create_tables():
    db.create_all()

# Create a welcome endpoint
@app.route('/')
def index():
    return "Welcome to the Task Manager API"

# Unified endpoint for bulk and single task creation
@app.route('/v1/tasks', methods=['POST'])
def bulk_add_tasks():
    data = request.get_json()
    tasks_data = data.get("tasks", [])
    
    tasks = []
    validation_errors = []
    
    for index, task_data in enumerate(tasks_data):
        try:
            validated_task_data = TaskCreate(**task_data)
            task = Task(title=validated_task_data.title, is_completed=validated_task_data.is_completed)
            tasks.append(task)
        except ValidationError as e:
            validation_errors.append({
                "index": index,
                "errors": e.errors(),
                "input": task_data
            })
    
    if validation_errors:
        return jsonify(errors=validation_errors), 400

    # Bulk save tasks and commit
    db.session.bulk_save_objects(tasks)
    db.session.commit()
    
    # Return the IDs of the newly created tasks
    return jsonify(tasks=[{"id": task.id} for task in tasks]), 201

# List all tasks
@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    return TaskList(tasks=[task.to_dict() for task in tasks]).json(), 200

# Get a specific task
@app.route('/v1/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return task.to_dict(), 200

# Delete a specific task
@app.route('/v1/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

# Edit a specific task
@app.route('/v1/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    try:
        task_data = TaskUpdate(**data)
    except ValidationError as e:
        return jsonify(errors=e.errors()), 400

    task.title = task_data.title
    task.is_completed = task_data.is_completed
    db.session.commit()
    return '', 204

# Bulk delete tasks
@app.route('/v1/tasks', methods=['DELETE'])
def bulk_delete_tasks():
    data = request.get_json()
    ids = [task["id"] for task in data.get("tasks", [])]
    Task.query.filter(Task.id.in_(ids)).delete(synchronize_session=False)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
