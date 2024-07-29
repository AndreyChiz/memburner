.PHONY: examination_service_dev_comands


run_db_conatainer:
	docker-compose up -d

run_app:
	./.venv/bin/python ./service/main.py



migration_autogenerate:
	cd service && alembic revision --autogenerate 

migration_upgrade_db:
	cd service && alembic upgrade head


migration_downgrade_db:
	cd service && alembic downgrade base


check_all:
	cd service && alembic downgrade base
	cd service && alembic upgrade head
	cd service && python -m src.exam_service.crud