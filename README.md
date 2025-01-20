# FIAP - Tech Challenge 01

# Arquitetura

![Arquitetura Simplificada](./docs/architecture.jpg)
Board Miro: https://miro.com/app/board/uXjVL7Z2f4M=/?share_link_id=93685718113

# Infraestrutura

A infraestrutura é criada através do Terraform (disponível no diretório `tf`):

- Criar um cluster Aurora PostgreSQL
- Criar um bucket S3
- Criar uma tabela no banco de dados Aurora
- Criar uma instancia EC2 para execução da aplicação

# Scraping 

A aplicação scraping é responsável pela extração dos dados do site da Embrapa e armazenamento no BD. Os processos de carga serão agendados para execução periódica.

## Modelo de dados

O banco de dados que vai armazenar o dados será o Aurora PostgreSQL, da AWS.

Para cada tipo de dados será criada uma tabela. A gestão do modelo de dados é realizado pelo pacote `alembic`,

## Carga de dados.


# API

A aplicação Python será responsável por:

- Expor uma API registro de usuários
- Expor uma API geração de token do usuário
- Expor uma APIs para consulta dos dados por tipo e ano

```bash
poetry run python app/main.py
```

# Especificação API

A especificação da API está no arquivo `api_spec.yaml`

https://github.com/smatioli/fiap-tech-challenge-01
Ela pode ser visualizada no Swagger: https://editor.swagger.io/?url=https://raw.githubusercontent.com/smatioli/fiap-tech-challenge-01/main/api_spec.yaml

# Analytics

Detalhamento das visões analíticas com PBI, pode ser acessado no link:

https://app.powerbi.com/view?r=eyJrIjoiMTVhNTEwNDUtYTk4Yy00ODJhLTljOTAtODY3N2QzODhmMTc3IiwidCI6ImE5ZWYzOTU5LThiOTYtNGVlMC05MjNjLTFkODlhZDk2OWNmOSJ9


