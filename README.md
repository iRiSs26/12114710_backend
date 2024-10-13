Task Manager API
Description
This is a Task Manager API built with Flask and SQLAlchemy. It allows users to create, read, update, and delete tasks. The API supports bulk operations for both creating and deleting tasks, making it efficient for managing multiple tasks at once.

Features
Create Tasks: Add single or multiple tasks in one request.
Read Tasks: Fetch all tasks or get details of a specific task by ID.
Update Tasks: Edit task details such as title and completion status.
Delete Tasks: Remove a specific task or delete multiple tasks at once.
Validation: Utilizes Pydantic for input validation.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/your-repo.git
Navigate to the project directory:
bash
Copy code
cd your-repo
Create a virtual environment:
bash
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Usage
Set up the database by running the following command:
bash
Copy code
flask db upgrade
Start the Flask server:
bash
Copy code
flask run
Use a tool like Postman to test the API endpoints.
API Endpoints
POST /v1/tasks: Create new tasks.
GET /v1/tasks: Retrieve all tasks.
GET /v1/tasks/{id}: Get a specific task by ID.
PUT /v1/tasks/{id}: Update a specific task.
DELETE /v1/tasks/{id}: Delete a specific task.
DELETE /v1/tasks: Bulk delete tasks.
