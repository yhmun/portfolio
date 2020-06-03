### Prerequisite
- Make sure that the python3 package is installed.
- Change a working directory

### Creating a virtual environment
```
$ python3 -m venv venv
```

### Activating the virtual environment
- Regardless of which version of Python you are using, when the virtual environment is activated, you should use the pip command (not pip3)
```
$ source venv/bin/activate
```

### Upgragding python package installer 
```
(venv) $ pip install --upgrade pip
```

### Installing Django
```
(venv) $ pip install django
```

### Freezing installed packages in requirements format
```
(venv) $ pip freeze > requirements.txt
```

### Installing dependecies from requirements file
```
(venv) $ pip install -r requirements.txt
```

### Deactivating the virtual environment
```
(venv) $ deactivate
```

### Packages
```
(venv) $ pip install django                 # A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
       - pip install asgiref                # ASGI specs, helper code, and adapters
       - pip install pytz                   # World timezone definitions, modern and historical
       - pip install sqlparse               # Non-validating SQL parser
(venv) $ pip install psycopg2-binary        # psycopg2 - Python-PostgreSQL Database Adapter
(venv) $ pip install djangorestframework    # Web APIs for Django, made easy.
(venv) $ pip install Pillow                 # Python Imaging Library (Fork)
```

### Creating a project
```
(venv) $ django-admin startproject portfolio .

(venv) $ tree .
├── manage.py
├── portfolio
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
```

### File Structure
```
brew install tree
sudo apt-get install tree -y

```

### The development server
```
(venv) $ python manage.py runserver 0:8000
``` 

### Creating your own app
```
(venv) $ python manage.py startapp main
(venv) $ tree main
main/
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

### Changing App Settings
```
(venv) $ vi app/settings.py
...
import environ
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': env.db()
}

TIME_ZONE = env('TIME_ZONE')
...
```

### Database Migration
```
(venv) $ python manage.py makemigrations polls
(venv) $ python manage.py sqlmigrate polls 0001
(venv) $ python manage.py migrate
(venv) $ python manage.py showmigrations
(venv) $ python manage.py migrate --fake projects zero
(venv) $ python manage.py migrate projects zero
```

### Shell
```
>>> from polls.models import Choice, Question

>>> Question.objects.all()

>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()

>>> Question.objects.filter(id=1)
>>> Question.objects.filter(question_text__startswith='What')

>>> Question.objects.get(pk=1)

>>> q.choice_set.all()
>>> q.choice_set.create(choice_text='The sky', votes=0)
>>> q.choice_set.count()
>>> c.delete()
```

### Creating an admin user
```
(venv) $ python manage.py createsuperuser
```

### curl command
```
(venv) $ curl -sS http://127.0.0.1:8000/receipts/ | python -m json.tool
(venv) $ curl -H "Content-Type: application/json" http://localhost:8000/receipts -d '{}'
```



