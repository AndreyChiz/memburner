.PHONY: examination_application_dev_comands

#---------------install---------------

# dont forget about .env file
run_db_conatainer:
	docker-compose up -d

migration_upgrade_db:
	cd application && alembic upgrade head

run_app:
	find . -type d -name '__pycache__' -exec rm -r {} + && \
	export PYTHONDONTWRITEBYTECODE=1 && \
	 ./.venv/bin/python ./application/main.py

# ----------------dev-----------------

migration_autogenerate:
	cd application && alembic revision -m "initial" --autogenerate 



migration_downgrade_db:
	cd application && alembic downgrade base


check_all:
	cd application && alembic downgrade base
	cd application && alembic upgrade head
	cd application && python -m src.exam_application.crud

clear_pycache:
	export PYTHONDONTWRITEBYTECODE=1
	find . -type d -name '__pycache__' -exec rm -r {} + 