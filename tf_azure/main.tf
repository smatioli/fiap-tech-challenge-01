# Configure Azure Provider
provider "azurerm" {
  features {}
  subscription_id = var.azure_subscription_id
}

# Create Resource Group
resource "azurerm_resource_group" "rg" {
  name     = var.azure_resource_group_name
  location = var.azure_region
  
  tags = var.tags
}

output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}
