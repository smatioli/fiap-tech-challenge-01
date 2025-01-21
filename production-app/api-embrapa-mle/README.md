# api_embrapa_mle

Para executar a API localmente:

pip install poetry

poetry shell

poetry install

uvicorn app.main:app

# iniciar a aplicação na aws

cd /home/ec2-user/app/fiap-tech-challenge-01/production-app/api-embrapa-mle
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000

