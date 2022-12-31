	
## Running project

Create base dir and env.

	mkdir coding_club_base && cd coding_club_base
	python3 -m venv env
	source env/bin/activate

Clone project to your machine.

	git clone  https://github.com/bhuvishi/coding_club.git
	cd coding_club

Install require packages

	pip install -r requirements.txt

Migrate project

	python3 manage.py makemigrations
	python3 manage.py migrate
		
Run your server on your localhost

	python3 manage.py runserver

Zappa deploy

	export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
	export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
	zappa deploy dev
	zappa update dev
	python manage.py collectstatic
	zappa manage dev "collectstatic --noinput"

