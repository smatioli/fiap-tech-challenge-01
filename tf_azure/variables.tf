variable "azure_subscription_id" {
  description = "Azure subscription ID"
  type        = string
}

variable "azure_resource_group_name" {
  description = "Azure resource group name"
  type        = string
  default     = "fiap-tech-challenge"
}

variable "azure_region" {
  description = "Azure region"
  type        = string
  default     = "East US 2"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "fiap-tech-challenge"
}

variable "tags" {
  description = "Tags"
  type        = map(string)
  default     = {
    environment = "dev"
  }
}

variable "db_admin_username" {
  description = "PostgreSQL administrator username"
  type        = string
  sensitive   = true
}

variable "db_admin_password" {
  description = "PostgreSQL administrator password"
  type        = string
  sensitive   = true
}

variable "db_name" {
  description = "Name of the database to create"
  type        = string
  default     = "myapp_dev"
}