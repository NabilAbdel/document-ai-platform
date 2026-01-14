cd c:\my_data\projects\document_ai_platform

OPENAI_API_KEY=<enter api key>
GCP_PROJECT_ID=<enter api key>
DOC_AI_PROCESSOR_ID=<enter docai prrocessor generated id>
GOOGLE_APPLICATION_CREDENTIALS=<enter google creds>

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env

uvicorn api.main:app --reload
