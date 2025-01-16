# Task Management API

This is a Task Management API built with Django and Django REST Framework. The API allows users to manage their tasks, including creating, updating, and deleting tasks. It also supports user authentication using JWT tokens.

## Project Structure

- `__init__.py`: Initializes the TaskMGMT_API module.
- `asgi.py`: ASGI configuration for the project.
- `exceptions.py`: Custom exception handling for the project.
- `settings.py`: Django settings for the project.
- `urls.py`: URL routing for the project.
- `wsgi.py`: WSGI configuration for the project.

## Settings

The `settings.py` file contains all the necessary configurations for the Django project, including:

- **BASE_DIR**: Base directory of the project.
- **ALLOWED_HOSTS**: Hosts allowed to access the project.
- **STATIC_ROOT**: Directory for static files.
- **STATICFILES_STORAGE**: Storage backend for static files.
- **SECRET_KEY**: Secret key for the project.
- **DEBUG**: Debug mode setting.

## Deployment

The project is configured to be deployed on Heroku. The `django_heroku` settings are included for this purpose.

## Custom Exception Handling

Custom exception handling is implemented in the `exceptions.py` file.

## License

This project is licensed under the MIT License.