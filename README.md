# D3-Django integration

Sample project to help who want to integrate D3 getting data from Django.

Companion repository of the StackOverflow answer: [Passing data from Django to D3](http://stackoverflow.com/a/26455798/585592).

Questions? Please let me know!

Best regards!


## Quickstart

Clone this repository.

Install requirements:

    pip install -r requirements.txt


Migrate:

    python manage.py migrate


Create a superuser:

    python manage.py createsuperuser

Run the development server:

    python manage.py runserver


Log into admin and add some Play instances (sample data).

    http://localhost:8000/admin/

See your graph at root url:

    http://localhost:8000/
