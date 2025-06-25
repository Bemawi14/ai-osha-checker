from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

from doc_parser import extract_text_from_file
from osha_rules import check_osha_reportability

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only — use ["http://localhost:3000"] or similar in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_document(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract text
        text = extract_text_from_file(temp_path)

        # Run through OSHA rule checker
        result = check_osha_reportability(text)

        # Clean up
        os.remove(temp_path)

        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
