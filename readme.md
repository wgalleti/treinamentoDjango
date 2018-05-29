# Preparação do ambiente

Antes de executarmos os comandos, vamos preparar nosso banco dados e algumas configurações.

Primeiramente, estamos utilizando o jupyter notebook, ele ira nos auxiliar em nosso treinamento. Vale a pena uma [leitura](https://jupyter-notebook.readthedocs.io/en/stable/)

Agora, vamos iniciar um ambiente virtual e importar nosso projeto:

```bash
# clonar o projeto Git
git clone git@github.com:wgalleti/treinamentoDjango.git
cd treinamentoDjango.git

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

Agora que temos as dependencias, configure seu banco de dados preferido no `settings.py` e vamos importar alguns dados iniciais que nos ajudarão em algumas etapas

```bash
python manage.py loaddata data.json
```