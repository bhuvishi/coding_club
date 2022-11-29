	
## Running project

# Create base dir and env.
	mkdir coding_club_base && cd coding_club_base
	python -m venv env
	source env/bin/activate

Clone project to your machine.

	git clone  https://github.com/bhuvishi/coding_club.git

Install require packages
	pip install Django==2.1.9 djangorestframework==3.10.0 zappa
	pip install django-s3-storage
	pip install -r requirements.txt

Migrate project

	python3 manage.py makemigrations
	python3 manage.py migrate
		
Run your server on your localhost

	python3 manage.py runserver


zappa init
zappa deploy dev

