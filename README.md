## Portflio Web Application
This purposes for practising builing web applicaiton on cloud.

## Prerequisite 
- Ubuntu 18.04 LTS (option)
- Docker CE
- Docker-Compose

## Getting Started
- Download source codes
```
$ git clone https://github.com/mcodegeeks/portfolio.git
$ cd portfolio
```
- Create environmental files
```
$ vi .env.db
POSTGRES_USER=<postgres>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<portfolio>
```
```
$ vi .env
DEBUG=False
SECRET_KEY=<encripted password>
DJANGO_ALLOWED_HOSTS=<domain name> localhost 127.0.0.1 [::1]
DATABASE_URL=postgresql://<postgres>:<password>@db:5432/<portfolio>
TIME_ZONE=<America/Toronto>
```
- Launch servers
```
$ docker-compose up -d                              # for development
$ docker-compose -f docker-compose.prod.yml up -d   # for production
```
- Create admin user
```
$ docker-compose exec web python manage.py createsuperuser
```
- Migrate database
```
$ docker-compose exec web python manage.py migrate
```
- Explore on your web browser
  * http://example.com
  * http://example.com/admin

## Getting Started for standalone development
- Create environmental file
```
$ vi web/portflio/.env
DEBUG=True
SECRET_KEY=<encripted password>
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DATABASE_URL=postgresql://<postgres>:<password>@localhost:54320/<portfolio>   # Port: 54320
TIME_ZONE=<America/Toronto>
```
- Launch postgres server only
```
$ docker-compose up postgres
```
- Have fun with developement
```
$ cd web
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py createsuperuser
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver 0:8000
```
- Explore on your web browser
  * http://localhost:8000
