resource "aws_cloudwatch_log_group" "ecs_logs" {
  name              = "/ecs/embrapa-api"
  retention_in_days = 30  
}