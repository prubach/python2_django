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
