all::
	@exit 0

push::
	dotcloud push --all diag2img

logs::
	dotcloud logs diag2img.www

ssh::
	dotcloud ssh diag2img.www

restart::
	dotcloud restart diag2img.www
run::
	(cd mysite; ./manage.py runserver)
