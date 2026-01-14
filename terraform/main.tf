provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_service" "doc_ai" {
  name     = "doc-ai-platform"
  location = var.region

  template {
    spec {
      containers {
        image = var.image_url
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}
