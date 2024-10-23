# IT Company Task Manager

**IT Company Task Manager** is a web-based application designed to help companies manage tasks internally, built using the Django framework. It allows companies to create, assign, and track tasks for employees and view details about each worker.

## Features
- **User Authentication**: Log in and sign up with Django's built-in authentication system.
- **Employee Management**: Add, edit, and delete employee information.
- **Task Management**: Create, edit, delete tasks, and assign them to employees.
- **Employee Detail Page**: View details about each employee, including completed tasks.
- **Pagination Support**: Pagination for task and employee lists.
- **AdminLTE Interface**: AdminLTE for enhanced control panel design.

## Technologies Used
- **Python 3.8+**
- **Django 4.1**
- **SQLite3** (default database)
- **Bootstrap 4** for responsive design
- **Django Crispy Forms** for form handling
- **AdminLTE** for admin interface design

## Prerequisites
- Python 3.8+
- pip
- virtualenv

## Setting Up the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/it-company-task-manager.git
    ```

2. Navigate into the project directory:
    ```bash
    cd it-company-task-manager
    ```

3. Create a virtual environment:
    ```bash
    python -m venv new_venv
    ```

4. Activate the virtual environment:
    - For Windows:
      ```bash
      new_venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      source new_venv/bin/activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Create an `.env` file based on `.env.sample` and set environment variables, including `SECRET_KEY`.

7. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

8. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Project Structure
- `it_company_task_manager/`: Main Django project settings.
- `task_manager/`: App for task and employee management.
- `static/`: Static files (CSS, JS, images).
- `templates/`: HTML templates.
- `.env`: Environment variables (make sure it is listed in `.gitignore`).
- `requirements.txt`: List of project dependencies.

## License
This project is licensed under the MIT License. Feel free to use and modify it.

