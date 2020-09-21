requirements:  

- mariadb or mysql

mysql isn't necessary for local development but until I figure out how to split requirements between dev/prod, it's necessary to include mysqlclient which requires a local installation
I'm using npm in place of yarn because this is meant to work on pythonanywhere.com, which does not support yarn at this time.

deployment to a new server:

fill out settings/example.py, renaming to something appropriate
then update os.environ.setdefault in wsgi.py / asgi.py / manage.py if necessary.
pip install -r requirements.txt

## pythonanywhere

when your code has been uploaded to the server (git or direct upload), enter the source code directory under Web.

in the terminal, run `$ mkvirtualenv <name-of-virtualenv>` before installing with pip. Use `$ workon <name-of-virtualenv>` to reactivate your virtualenv later.

make sure to add the static directory to your web server settings, something like:

URL         | Directory
---         | ---------
`/static/`  | `/home/<username>/django_template/django_template/staticfiles`
`/media/`   | `/home/<username>/django_template/django_template/media`


then in the terminal, run `$ python manage.py collectstatic`  
this is necessary to gather any static files provided by packages, such as Django's admin styles & scripts.