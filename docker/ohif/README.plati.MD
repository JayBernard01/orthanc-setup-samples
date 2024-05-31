# steps (inside the dir ohif)
```bash
poetry install
poetry shell
poetry run python3 main.py
exit
```
## run python server for plati
```bash
poetry run python3 ./plati/manage.py runserver 0.0.0.0:8000
```

## to setup database -> use docker postgress db -> create a .env file and run in the same dir
```bash
docker run -d --name plati-db-standalone --env-file .env -p 5432:5432 postgres:latest
```
## to run database
```bash
docker start plati-db-standalone
```
## migrate configurations of db
```bash
poetry run python3 ./plati/manage.py migrate
```
## usefull command to migrate to bd schema ORM
```bash
poetry run python3 ./plati/manage.py makemigrations polls
```