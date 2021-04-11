### Task manager API

### Running:

buikd and run:
```sh
docker-compose up --build
```
migration
```sh
docker-compose -f docker-compose.yml exec web python manage.py migrate
```
tests
```sh
python3 manage.py runserver
```

Swagger: http://localhost:8000/swagger/ (local)