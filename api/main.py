from fastapi import FastAPI, UploadFile
from orchestrator.pipeline import run_pipeline
import tempfile

app = FastAPI()

@app.post("/process")
async def process(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        return run_pipeline(tmp.name)
