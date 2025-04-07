web: gunicorn webapp-khwebsite.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn webapp-khwebsite.wsgi