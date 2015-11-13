# article club

## Installation

1. Clone this repo into a fresh virtual environment
2. Install reqs via Pip

```shell
$ pip install -r requirements.txt
```

3. Create Postgres database

```shell
$ createdb articleclub
```

4. Set up `local_settings.py` with development environment specifics

```python
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'articleclub',
    }
}
```

5. Run `migrate` command (inside Django project) to terraform database

```shell
$ ./manage migrate
```

6. Start server

```shell
$ ./manage.py runserver
```

... and then visit [http://localhost:8000/](http://localhost:8000/)
