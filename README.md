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

![Screenshot: Home page](http://vero4ka.info/static/images/docs/shop1.png)

![Screenshot: Make an order](http://vero4ka.info/static/images/docs/shop2.png)

![Screenshot: Edit profile](http://vero4ka.info/static/images/docs/shop3.png)

![Screenshot: Orders list](http://vero4ka.info/static/images/docs/shop4.png)

![Screenshot: Admin](http://vero4ka.info/static/images/docs/shop5.png)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/ctrl-alt-delete/burger_shop/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

