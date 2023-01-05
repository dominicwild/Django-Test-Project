# How to Run Server
`python manage.py runserver`

# How to create an app
`python manage.py startapp polls`

## Creating Database Tables
Some apps containing in `settings.py` under `INSTALLED_APPS` need database tables in order to operate properly. 

Run:

`python manage.py migrate`

In order to create them.

### Making Migrations
In order to make migrations run:

`python manage.py makemigrations <appName>`

## Interactive Shell
Running:

`python manage.py shell`

Will open the interactive shell for Python with Django. 
One thing tt allows is querying the database with the models and saving them.

I.e.,
```python
from polls.models import Choice, Question

Question.objects.all()

from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
```

## Projects vs Apps
An app is a web application that does something – e.g., 
a blog system, a database of public records or a small poll app. 

A project is a collection of configuration and apps for a particular website. 
A project can contain multiple apps. An app can be in multiple projects.

### Adding an App
In order to add an app its dotted path should be included in the `INSTALLED_APPS` array in `settings.py` of the project. 

The configuration is a class usually contained in `apps.py` e.g., for polls it is PollsConfig.


## Details
- Default database used is SQLite