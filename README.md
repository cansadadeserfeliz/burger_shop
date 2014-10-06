Burger online ordering platform
===============================

Django Test Project for a burger online ordering platform


Description
-----------

As a customer, I need to:

* Enter my contact & delivery details
* Choose the ingredients I want in my burgers
* See the final price
* Place an order

As the manager/cook, I need to:

* See the orders.
* Set/change the status of orders (ordered, in progress, on the road, delivered).
* Filter by order status.
* Do all the above only when logged in.

Installation
------------

    git clone https://github.com/ctrl-alt-delete/burger_shop.git
    pip install -r requirements.txt
    touch app/local_settings.py

Define your local settings in ``local_settings.py``, for example,

    DEBUG = True
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'burger_shop',
        }
    }

Run migrations:

    python manage.py migrate
    
Run server:

    python manage.py runserver

Screenshots
-----------

![Screenshot: Home page](http://i.imgur.com/5uyIIrM.png)

![Screenshot: Make an order](http://i.imgur.com/C5sYDXQ.png)

![Screenshot: Edit profile](http://i.imgur.com/jEKirk7.png)

![Screenshot: Orders list](http://i.imgur.com/MebAfv3.png)

![Screenshot: Admin](http://i.imgur.com/XgOl0Vy.png)
