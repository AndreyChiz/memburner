.PHONY: examination_service_dev_comands


run_db_conatainer:
	docker-compose up -d

run_app:
	./.venv/bin/python ./service/main.py


migration_autogenerate:
	alembic revision --autogenerate    

migration_upgrade_db:
	alembic upgrade head


migration_downgrade_db:
	alembic downgrade base


check_all:
	alembic downgrade base
	alembic upgrade head
	python -m src.exam_service.crud