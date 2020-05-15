# Installation
Assuming you use virtualenv, follow these steps to download and run the
e-learning application in this directory:

    $ git clone ****
    $ cd online_study_mangement_system
    $ virtualenv venv
    $ activate your virtual environment
    $ pip install -r requirements
    $ python manage.py migrate
    $ python manage.py runserver

# Compatibility
* Python 2.7
* Django 1.9
* SQLite
