variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name to be used for resource naming"
  type        = string
  default     = "fiap"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "db_username" {
  description = "Database master username"
  type        = string
  default     = "postgres"
}

variable "db_password" {
  description = "Database master password"
  type        = string
  sensitive   = true
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "fiap_tech_challenge_db"
}

variable "private_subnet_cidr_a" {
  description = "CIDR block for private subnet in AZ a"
  type        = string
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr_b" {
  description = "CIDR block for private subnet in AZ b"
  type        = string
  default     = "10.0.2.0/24"
}

variable "private_subnet_cidr_c" {
  description = "CIDR block for private subnet in AZ c"
  type        = string
  default     = "10.0.3.0/24"
}

variable "public_subnet_cidr_a" {
  description = "CIDR block for public subnet in AZ a"
  type        = string
  default     = "10.0.4.0/24"
}

variable "public_subnet_cidr_b" {
  description = "CIDR block for public subnet in AZ b"
  type        = string
  default     = "10.0.5.0/24"
}

variable "public_subnet_cidr_c" {
  description = "CIDR block for public subnet in AZ c"
  type        = string
  default     = "10.0.6.0/24"
} 

variable "db_host" {
  description = "Database host"
  type        = string
  sensitive   = true
}


variable "secret_key" {
  description = "Secret key"
  type        = string
  sensitive   = true
}

variable "algorithm" {
  description = "Algorithm"
  type        = string
  default     = "HS256"
}