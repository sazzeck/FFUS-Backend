MANAGE := python3 ffus/manage.py

dev:
	$(MANAGE) runserver

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

