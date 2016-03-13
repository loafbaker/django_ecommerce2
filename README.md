django_ecommerce2
=================

An improved e-commerce app built within django framework

Run in django 1.9.4 and python 2.7.6

# Setup

Install all the required libraries

    pip install -r requirements.txt

Rebuild database

    rm db.sqlite3
    python manage.py migrate
    python manage.py createsuperuser

Collect static files

    python manage.py collectstatic

Run web server

    python manage.py runserver

Finally, you can view the web app with your local browser by accessing http://localhost:8000/

# Version Control

Ver.1   [Basic Template](../../tree/086876c197cec682ba202168e2260eda4a942be9)

Ver.2   [Products App](../../tree/4f3251004f29b20addc412802afc5ccb3dd2e258)

Ver.3   [Product Detail View](../../tree/9d01d36277152bbfb7ec3d8b9e79af0694c83b0d)