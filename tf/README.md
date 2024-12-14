# Terraform para criação da infraestrutura do projeto

## Prerequisites

- AWS CLI
- Terraform
- AWS credentials

## Configuração do ambiente

1. Configure as variáveis de ambiente AWS:

```bash
aws configure --profile fiap-tech-challenge
```

2. Execute o Terraform para criar a infraestrutura:

```bash
terraform init
terraform apply
```

3. Para criar as tabelas no banco de dados instalar:

```bash
brew install libpq
```
