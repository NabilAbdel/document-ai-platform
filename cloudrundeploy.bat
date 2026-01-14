docker build -t gcr.io/YOUR_PROJECT/doc-ai .
docker push gcr.io/YOUR_PROJECT/doc-ai

cd terraform
terraform init
terraform apply
