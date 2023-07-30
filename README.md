gcloud builds submit --tag gcr.io/central-cinema-394002/armstrong-data-solutions --project=central-cinema-394002

gcloud run deploy --image gcr.io/central-cinema-394002/armstrong-data-solutions --platform managed --project=central-cinema-394002 --allow-unauthenticated