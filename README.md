# api_yamdb - API для проекта YaMDb

## Описание

Проект YaMDb собирает отзывы пользователей на различные произведения: о фильмах, книгах, музыке.


### Технологии

Python, Django, PostgreSQL, Simple JWT, git

### Шаблон наполнения env-файла

```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
SECRET_KEY=secretkey
```

### Запуск приложения в контейнерах

Запуск docker-compose:

```bash
docker-compose up -d
```

Выполнить миграции:

```bash
docker-compose exec web python manage.py migrate
```

Создать суперюзера:

```bash
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

```bash
docker-compose exec web python manage.py collectstatic --no-input
```

### Заполнение базы данными

```bash
docker-compose exec web python manage.py loaddata fixtures.json
```
