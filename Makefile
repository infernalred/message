migr:
	docker-compose run --rm web sh -c "python manage.py migrate"
super:
	docker-compose run --rm web sh -c "python manage.py createsuperuser"