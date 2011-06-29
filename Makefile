all::
	@exit 0

push::
	dotcloud push diag2img

run::
	(cd mysite; ./manage.py runserver)
