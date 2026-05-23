0)pip freeze > requirements.txt
1)Клонуйте проект
2) python -m venv venv
3) Активуйте оточення venv\Scripts\activate
4) pip install -r requirements.txt
5) pip install whitenoise
6) MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
7)python manage.py collectstatic 