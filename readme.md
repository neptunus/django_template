I'm using npm in place of yarn because this is meant to work on pythonanywhere.com, which does not support yarn at this time.

deployment to a new server:

fill out settings/example.py, renaming to something appropriate, then update os.environ.setdefault in wsgi.py / asgi.py / manage.py if necessary.
pip install -r requirements.txt

