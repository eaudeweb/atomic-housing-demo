Development
===========

1. Clone this repo.
2. Setup virtualenv::

    virtualenv env
    source env/bin/activate

3. Install requirements::

    pip install -r requirements.txt

4. Database::

    python manage.py syncdb

5. Run server::

    python manage.py runserver

6. Load fixtures::

    python manage.py loaddata sample
