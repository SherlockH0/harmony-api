.PHONY: install 
install:
	poetry install

.PHONY: migrate
migrate: 
	poetry run python -m you_project_name.manage migrate

.PHONY: migrations 
migrations: 
	poetry run python -m you_project_name.manage makemigrations
	
.PHONY: runserver
runserver:
	poetry run python -m you_project_name.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m you_project_name.manage createsuperuser

.PHONY: update
update: install migrate ;
