resource "null_resource" "create_table" {
  provisioner "local-exec" {
    command = <<EOT
    PGPASSWORD='${var.db_password}' psql \
      -h ${aws_rds_cluster.aurora.endpoint} \
      -U ${var.db_username} \
      -d ${var.db_name} \
      -c "CREATE TABLE production (
            group VARCHAR(255) NOT NULL,
            product VARCHAR(255) NOT NULL,
            year INT NOT NULL,
            qty FLOAT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
          );"
    EOT
  }
  depends_on = [aws_rds_cluster.aurora]
}