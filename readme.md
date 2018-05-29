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

+-------------+-----------------------------------------------+--------------------------------------------------+
| Engine      | Django Backend                                | URL                                              |
+=============+===============================================+==================================================+
| PostgreSQL  | ``django.db.backends.postgresql_psycopg2``    | ``postgres://USER:PASSWORD@HOST:PORT/NAME`` [1]_ |
+-------------+-----------------------------------------------+--------------------------------------------------+
| PostGIS     | ``django.contrib.gis.db.backends.postgis``    | ``postgis://USER:PASSWORD@HOST:PORT/NAME``       |
+-------------+-----------------------------------------------+--------------------------------------------------+
| MSSQL       | ``sql_server.pyodbc``                         | ``mssql://USER:PASSWORD@HOST:PORT/NAME``         |
+-------------+-----------------------------------------------+--------------------------------------------------+
| MySQL       | ``django.db.backends.mysql``                  | ``mysql://USER:PASSWORD@HOST:PORT/NAME``         |
+-------------+-----------------------------------------------+--------------------------------------------------+
| MySQL (GIS) | ``django.contrib.gis.db.backends.mysql``      | ``mysqlgis://USER:PASSWORD@HOST:PORT/NAME``      |
+-------------+-----------------------------------------------+--------------------------------------------------+
| SQLite      | ``django.db.backends.sqlite3``                | ``sqlite:///PATH`` [2]_                          |
+-------------+-----------------------------------------------+--------------------------------------------------+
| SpatiaLite  | ``django.contrib.gis.db.backends.spatialite`` | ``spatialite:///PATH`` [2]_                      |
+-------------+-----------------------------------------------+--------------------------------------------------+
| Oracle      | ``django.db.backends.oracle``                 | ``oracle://USER:PASSWORD@HOST:PORT/NAME`` [3]_   |
+-------------+-----------------------------------------------+--------------------------------------------------+
| Oracle (GIS)| ``django.contrib.gis.db.backends.oracle``     | ``oraclegis://USER:PASSWORD@HOST:PORT/NAME``     |
+-------------+-----------------------------------------------+--------------------------------------------------+
| Redshift    | ``django_redshift_backend``                   | ``redshift://USER:PASSWORD@HOST:PORT/NAME``      |
+-------------+-----------------------------------------------+--------------------------------------------------+

.. [1] With PostgreSQL, you can also use unix domain socket paths with
       `percent encoding <http://www.postgresql.org/docs/9.2/interactive/libpq-connect.html#AEN38162>`_:
       ``postgres://%2Fvar%2Flib%2Fpostgresql/dbname``.
.. [2] SQLite connects to file based databases. The same URL format is used, omitting
       the hostname, and using the "file" portion as the filename of the database.
       This has the effect of four slashes being present for an absolute file path:
       ``sqlite:////full/path/to/your/database/file.sqlite``.
.. [3] Note that when connecting to Oracle the URL isn't in the form you may know
       from using other Oracle tools (like SQLPlus) i.e. user and password are separated
       by ``:`` not by ``/``. Also you can omit ``HOST`` and ``PORT``
       and provide a full DSN string or TNS name in ``NAME`` part.


```bash
python manage.py loaddata data.json
```