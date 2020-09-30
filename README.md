# coopsafe-crm-api

**SERVICE_NAME: crm-api**
 
**BUILD:**
<br />
docker-compose build 

**START:**
<br />
docker-compose up

**RUN PYTHON COMMANDS INSIDE DOCKER**
<br />
docker-compose run SERVICE_NAME sh -c ""

**RUN TEST**
<br />
docker-compose run --rm SERVICE_NAME sh -c "python manage.py test"

**RUN TEST WITH FLAKE8**
<br />
docker-compose run --rm SERVICE_NAME sh -c "python manage.py test && flake8"

**PEP8 FIX**
docker-compose run SERVICE_NAME sh -c "autopep8 --in-place --aggressive --aggressive PATH"

**SHOW ALL URLS**
<br />
docker-compose run --rm SERVICE_NAME sh -c "python manage.py show_urls"

---------
**Criar superusuario no django.**
<br />
docker-compose run --rm SERVICE_NAME sh -c "python manage.py createsuperuser"
<br />
<br />
**Acessar Admin do Django.**
<br />
O admin do django é acessível pela url: 127.0.0.1:8000/admin
<br />
<br />
**Acessar Api REST do Django.**
<br />
Acessar a documentação e teste da api REST: 127.0.0.1:8000/api/NOME_DO_PACOTE
<br />
<br />



