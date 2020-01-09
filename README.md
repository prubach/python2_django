# python2_django
1. Create new project on Github
2. git clone https://github.com/prubach/python2_django.git
3. cd python2_django
4. WINDOWS: 
		python -m venv venv
	UNIX:
		python3 -m venv venv
5. Activate:
WINDOWS:
venv\Scripts\activate
UNIX:
source venv/bin/activate

6. pip install django
or
pip3 install django
7. django-admin startproject bank
8. cd bank
9. python manage.py runserver
10. python manage.py startapp bankapp
11. After changes run:
python manage.py migrate
12. After changing models and adding app to INSTALLED_APPS in settings run:
 python manage.py makemigrations bankapp
13. python manage.py migrate
14. Play with shell:
python manage.py shell
In Shell:
>>> from bankapp.models import Customer, Account
>>> from django.utils import timezone
>>> c = Customer(first_name='John', last_name='Brown', email='john@brown', birth_date=timezone.now())
>>> c.save()

a = Account(balance=0, type='Debit', customer=c2)