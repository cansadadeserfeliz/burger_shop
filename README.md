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

    git clone https://github.com/vero4karu/burger_shop.git
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

![Screenshot: Home page](https://habrastorage.org/files/948/710/e06/948710e06ffb4bb7b82ed3418904ce54.png)

-------------

![Screenshot: Make an order](https://habrastorage.org/files/ebe/a76/136/ebea761361074802971dd9f040012992.png)

-------------

![Screenshot: Edit profile](https://habrastorage.org/files/842/ac2/a07/842ac2a0721d4d24914de19c94288aff.png)

-------------

![Screenshot: Orders list](https://habrastorage.org/files/572/a3d/f41/572a3df41d7747c1a1d71d83777255eb.png)

-------------

![Screenshot: Admin](https://habrastorage.org/files/7b2/c4e/ea5/7b2c4eea5ffd4b8a8592cba9de79a143.png)

