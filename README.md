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

Ver.4   [List View](../../tree/b94c4a912b42054ad3e6c9a08b476f6f001360de)

Ver.5   [Using Links for Model Instances](../../tree/40edd2c1b1ee6740c249f5e234f973586cb6b7dd)

Ver.6   [Model Managers](../../tree/6ec459823379f71cb35028449877ad8de58d0b11)

Ver.7   [Product Variations](../../tree/0a03b123da89698cb7ffb2b100745d2548bcc2a0)