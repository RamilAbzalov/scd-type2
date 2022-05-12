# Django SCD type 2 simple project

## Getting started

Create `.env` file with `.env.example` keys in `config` folder.

Install dependencies:
```shell
poetry install
```

Activate virtual environment:
```shell
poetry shell
```

Make database migrations:
```shell
python manage.py migrate
```

Create superuser for admin panel access:
```shell
python manage.py createsuperuser
```


Run server:
```shell
python manage.py runserver
```

## Admin panel
With superuser credentials you can sign in admin panel `http://localhost:8000/admin/`

## GraphQL

For testing API you can follow the link `http://localhost:8000/graphql/`


