resource "aws_secretsmanager_secret" "app_secrets" {
  name = "embrapa-api/env-vars"
}

# The actual secret values
resource "aws_secretsmanager_secret_version" "app_secrets" {
  secret_id = aws_secretsmanager_secret.app_secrets.id
  secret_string = jsonencode({
    DB_HOST = var.db_host
    DB_USER = var.db_username
    DB_PASSWORD = var.db_password
    DB_NAME = var.db_name
    SECRET_KEY = var.secret_key
    ALGORITHM = var.algorithm
  })
}


# # IAM policy to allow ECS to access Secrets Manager
# resource "aws_iam_role_policy" "secrets_policy" {
#   name = "ecs-secrets-policy"
#   role = aws_iam_role.ecs_agent.id

#   policy = jsonencode({
#     Version = "2012-10-17"
#     Statement = [
#       {
#         Effect = "Allow"
#         Action = [
#           "secretsmanager:GetSecretValue"
#         ]
#         Resource = [
#           aws_secretsmanager_secret.app_secrets.arn
#         ]
#       }
#     ]
#   })
# }