# Application

## API

```bash
cd scraping-api-mle

python -m venv venv

# Windows:
.\venv\Scripts\activate

# Unix/MacOS:
source venv/bin/activate
```

# API Aplicação

Para executar a API localmente:

```bash
cd api

pip install poetry

poetry shell

poetry install

uvicorn app.main:app
```


# API Scraping


```bash
cd scraping
```

1) Migrations

Para criar as tabelas no banco de dados, executar:



```bash
alembic init migrations

alembic revision --autogenerate -m "add tables"

alembic upgrade head
```


2) Executar o arquivo scraping.py

```bash
python scraping.py
```

3) Executar o arquivo main.py

```bash
python main.py
```
