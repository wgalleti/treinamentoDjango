# Preparação do ambiente

Antes de executarmos os comandos, vamos preparar nosso banco dados e algumas configurações.

Primeiramente, estamos utilizando o jupyter notebook, ele ira nos auxiliar em nosso treinamento. Vale a pena uma [leitura](https://jupyter-notebook.readthedocs.io/en/stable/)

Agora, vamos iniciar um ambiente virtual e importar nosso projeto:

```bash
# clonar o projeto Git
git clone git@github.com:wgalleti/treinamentoDjango.git
cd treinamentoDjango.git

# configure suas variaveis de ambiente
cp env.sample .env

# virtualenv
python -m venv .venv
pip install pipenv

# Windows
.venv\Scripts\activate

# Linux ou mac
source .venv\bin\activate

pipenv install
pipenv install --dev
```

Agora que temos as dependencias, configure seu banco de dados preferido no `.env` e vamos importar alguns dados iniciais que nos ajudarão em algumas etapas

Lembrando que estamos usando `dj-database-url`. Alguns exemplos de conexões:

URL schema
----------

| Engine      | Django Backend                                | URL                                              |
|-|-|
| PostgreSQL  | ``django.db.backends.postgresql_psycopg2``    | ``postgres://USER:PASSWORD@HOST:PORT/NAME`` |
| PostGIS     | ``django.contrib.gis.db.backends.postgis``    | ``postgis://USER:PASSWORD@HOST:PORT/NAME``       |
| MSSQL       | ``sql_server.pyodbc``                         | ``mssql://USER:PASSWORD@HOST:PORT/NAME``         |
| MySQL       | ``django.db.backends.mysql``                  | ``mysql://USER:PASSWORD@HOST:PORT/NAME``         |
| MySQL (GIS) | ``django.contrib.gis.db.backends.mysql``      | ``mysqlgis://USER:PASSWORD@HOST:PORT/NAME``      |
| SQLite      | ``django.db.backends.sqlite3``                | ``sqlite:///PATH``                        |
| SpatiaLite  | ``django.contrib.gis.db.backends.spatialite`` | ``spatialite:///PATH``                      |
| Oracle      | ``django.db.backends.oracle``                 | ``oracle://USER:PASSWORD@HOST:PORT/NAME``    |
| Oracle (GIS)| ``django.contrib.gis.db.backends.oracle``     | ``oraclegis://USER:PASSWORD@HOST:PORT/NAME``     |
| Redshift    | ``django_redshift_backend``                   | ``redshift://USER:PASSWORD@HOST:PORT/NAME``      |

[Duvidas](https://github.com/kennethreitz/dj-database-url)


```bash
python manage.py loaddata data.json
```