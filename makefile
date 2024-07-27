.PHONY: examination_service_dev_comands


run_db_conatainer:
	docker-compose up -d


migration_autogenerate:
	alembic revision --autogenerate    

migration_upgrade_db:
	alembic upgrade head


migration_downgrade_db:
	alembic downgrade base


#Команда для зпроверки запросов в базу данных
check_db_mamnger:
	python -m src.exam_service.crud


check_all:
	alembic downgrade base
	alembic upgrade head
	python -m src.exam_service.crud