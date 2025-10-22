# ToDoApp

1) Introduction
----------------

ToDoApp is a lightweight Django-based to-do list application that provides a simple REST API and an admin interface for managing tasks. It is designed as a starter project for learning Django and Django REST Framework, and as a foundation to build more advanced task-management features.

2) Features
-----------

- Create, read, update, and delete tasks (CRUD) via a REST API
- Admin interface to manage tasks and users
- Basic task fields: title, description, completed status, created/updated timestamps
- Uses Django ORM for storage (SQLite by default in development)
- Structured to easily add authentication and per-user task lists

Screenshot
----------

```
![Home screen](https://github.com/MinjunBark/ToDoApp/blob/a645fbabfd539ffbd39d7d8bc1661f5c6e50f092/docs/screenshots/Main_UI.png)
![Add and list tasks](https://github.com/MinjunBark/ToDoApp/blob/a645fbabfd539ffbd39d7d8bc1661f5c6e50f092/docs/screenshots/Adding_Task.png)
![Completed and deleted states](https://github.com/MinjunBark/ToDoApp/blob/a645fbabfd539ffbd39d7d8bc1661f5c6e50f092/docs/screenshots/Completed_Task.png)
```

To get started
--------------

Follow these steps to get the project running locally and to install the Django "task" app (the `tasks` app) so task models and admin are available.

1) Create and activate a virtual environment

```zsh
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies

```zsh
brew install python3
pip3 install django

# Creating the project
django-admin startproject --xyz--
cd --xyz--
python manage.py startapp tasks

```

3) Ensure the `tasks` app is installed in Django settings

Open `ToDoApp/settings.py` and make sure the `tasks` app is listed in `INSTALLED_APPS`, for example:

```python
INSTALLED_APPS = [
	# ... other installed apps ...
	'rest_framework',
	'tasks',  # make sure this line exists so the Task model and admin are discovered
]
```

4) Create and apply migrations for the `task` app

```zsh
# create migration files for the tasks app (if they don't already exist)
python3 manage.py makemigrations

# apply all migrations
python3 manage.py migrate
```


5) Create a superuser for the admin (if you need admin access)

```zsh
python3 manage.py createsuperuser
```

7) Run the development server

```zsh
python3 manage.py runserver
# then open http://127.0.0.1:8000/ in your browser
```

Notes
- If you change models, rerun `makemigrations` and `migrate`.

Tech stack
----------

- Backend: Django 5.x, Django REST Framework
- Database: SQLite (development default; replace with Postgres/MySQL in production)
- Frontend: Django templates and Bootstrap for UI styling
- Dev tools: Python 3.10+/venv, pip, optional pyenv/Homebrew
- Optional: Docker for containerized deployments

Django's MVT architecture (brief)
--------------------------------

Django follows the Model-View-Template (MVT) pattern, which is similar to MVC but adapted for web development:

- Model: represents the data structure and database schema. In this project, `tasks/models.py` defines the `Task` model. Models encapsulate data and business logic and map to database tables via Django's ORM.
- View: receives web requests, interacts with models, and returns responses. Views can return HTML templates (for the web UI) or serialized data (for APIs). In this project, `tasks/views.py` implements views that provide JSON responses for the REST API and/or render templates for pages.
- Template: the presentation layer — HTML files with template tags to render data supplied by views. Templates live in the `templates/` directory and are used to render the user interface.

Flow example (adding a task):

1. User fills the task form in the browser and submits.
2. A Django view receives the POST request and validates the incoming data.
3. The view creates a `Task` model instance and saves it to the database.
4. The view redirects to a page showing the updated task list rendered by a template.

MVT vs MVC note: Django's "view" is closer to the controller in MVC; templates are the view layer.


3) Future integrations
---------------------

Planned or possible future integrations and enhancements:

- User authentication and registration (JWT or session-based)
- Task due dates, reminders, and calendar integration
- Push notifications for due tasks (Firebase or Apple/Google push services)
- Sync with external calendar providers (Google Calendar, Outlook)
- Tagging, filtering, and search across tasks
- Webhooks and integrations with Zapier or IFTTT
- Docker containerization and production-ready deployment (Gunicorn + Nginx)

