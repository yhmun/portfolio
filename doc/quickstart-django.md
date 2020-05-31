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
(venv) $ pip install -r requirements
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
```

### Creating a project
```
(venv) $ django-admin startproject mysite .

(venv) $ tree .
├── manage.py
├── mysite
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

### Changing App Settings
```
(venv) $ vi app/settings.py
...
TIME_ZONE = 'America/Toronto'
...
```

### The development server
```
(venv) $ python manage.py runserver 0:8000
``` 

### Creating your own app
```
(venv) $ python manage.py startapp portfolio
(venv) $ tree portfolio
portfolio/
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```







