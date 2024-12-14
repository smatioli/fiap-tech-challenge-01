# DB Subnet Group
resource "aws_db_subnet_group" "aurora" {
  name       = "${var.project_name}-aurora-subnet-group"
  subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_b.id, aws_subnet.private_c.id]

  tags = {
    Name = "${var.project_name}-aurora-subnet-group"
  }
}

# Security Group for Aurora
resource "aws_security_group" "aurora" {
  name        = "${var.project_name}-aurora-sg"
  description = "Security group for Aurora PostgreSQL"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "PostgreSQL access"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # In production, restrict this to specific IPs
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-aurora-sg"
  }
}

# Aurora Cluster
resource "aws_rds_cluster" "aurora" {
  cluster_identifier     = "${var.project_name}-aurora-cluster"
  engine                = "aurora-postgresql"
  engine_version        = "14.6"  # Use latest compatible version
  database_name         = var.db_name
  master_username       = var.db_username
  master_password       = var.db_password
  skip_final_snapshot   = true  # Set to false in production
  db_subnet_group_name  = aws_db_subnet_group.aurora.name
  vpc_security_group_ids = [aws_security_group.aurora.id]

  tags = {
    Name = "${var.project_name}-aurora-cluster"
  }
}

# Aurora Instance
resource "aws_rds_cluster_instance" "aurora" {
  identifier         = "${var.project_name}-aurora-instance"
  cluster_identifier = aws_rds_cluster.aurora.id
  instance_class     = "db.t3.medium"  # Smallest instance class for Aurora
  engine            = aws_rds_cluster.aurora.engine
  engine_version    = aws_rds_cluster.aurora.engine_version

  tags = {
    Name = "${var.project_name}-aurora-instance"
  }
}
