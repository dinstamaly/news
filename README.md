# Extraction of News

#### Activate on docker our project

    1. Run the command: docker-compose up -d --build
    If don't work static in site 
    2. Collect all static files: docker-compose exec web python manage.py collectstatic --no-input --clear
    3. Create superuser if you need: docker-compose  exec web python manage.py createsuperuser
    4. Open your browse with link: http://localhost:8000/

#### If you haven't Docker and Docker-compose

You can install by following this link

### Docker

    https://docs.docker.com/engine/install/ubuntu/

### Docker-Compose

    https://docs.docker.com/compose/install/
