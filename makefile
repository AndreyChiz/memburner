.PHONY: examination_service_dev_comands

#---------------install---------------

# dont forget about .env file
run_db_conatainer:
	docker-compose up -d



migration_upgrade_db:
	cd service && alembic upgrade head

run_app:
	export PYTHONDONTWRITEBYTECODE=1 && \
	 ./.venv/bin/python ./service/main.py

# ----------------dev-----------------

migration_autogenerate:
	cd service && alembic revision -m "initial" --autogenerate 



migration_downgrade_db:
	cd service && alembic downgrade base


check_all:
	cd service && alembic downgrade base
	cd service && alembic upgrade head
	cd service && python -m src.exam_service.crud

clear_pycache:
	export PYTHONDONTWRITEBYTECODE=1