terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.15.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "app_image" {
  name = "todo-api:latest"
}

resource "docker_container" "app_container" {
  name  = "todo-api-container"
  image = docker_image.app_image.name
  ports {
    internal = 8000  # Change this to match the port your app listens on
    external = 8080  # This is the port you'll access locally (http://localhost:8080)
  }
}
