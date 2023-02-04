MANAGE := python3 ffus/manage.py

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

createsuperuser:
	$(MANAGE) createsuperuser --username="admin" --password="admin"