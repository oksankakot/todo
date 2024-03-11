# Todo List Application

This Todo List application allows users to manage their tasks and tags efficiently. Users can create, update, delete tasks and tags, mark tasks as completed, and assign tags to tasks. 

## Features

- **Task Management**: Users can create new tasks, update existing tasks, and delete tasks.
- **Tag Management**: Users can create new tags, update existing tags, and delete tags.
- **Task Status**: Users can mark tasks as completed or incomplete.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/todo-list.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application at [http://localhost:8000/](http://localhost:8000/)

## Technologies Used

- **Django**: The backend framework for building the application.
- **HTML/CSS**: Frontend styling and structure.
- **Bootstrap**: Frontend framework for responsive design.
