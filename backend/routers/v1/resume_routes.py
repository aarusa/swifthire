import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from dotenv import load_dotenv
from google import genai
import fitz
from pydantic import BaseModel
from typing import List
import schemas
from data.resumes import resumeData
from schemas import CandidateProfile

# Load Environment Variables
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

router = APIRouter()

# --------------- Resume Routes ------------------------
# Displaying resume list
@router.get("/list")
def get_resume_list():
    return resumeData

# Displaying single resume based on id
@router.get("/{id}")
def get_resume_by_id(id:int):
    for resume in resumeData:
        if resume["resume_id"] == id:
            return resume
        
    raise HTTPException(status_code=404, detail="Resume not found")
    # return resumeData[id]

# Adding a new resume
@router.post("/add")
async def add_resume(new_resume: schemas.Resume):
    resume_dict = new_resume.model_dump()

    if any(r['resume_id'] == resume_dict['resume_id'] for r in resumeData):
        raise HTTPException(status_code=400, detail="Resume already exists")
        
    resumeData.append(resume_dict)

    return {"message": "Resume added successfully", "data": resume_dict}


# Resume parsing
@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    # Read file content into memory
    # 'await' is used because file.read() is an asynchronous operation
    pdf_content = await file.read()

    # Open the PDF using PyMuPDF (fitz)
    # We use stream=pdf_content because the file is in memory, not saved on disk
    doc = fitz.open(stream=pdf_content, filetype="pdf")
    
    raw_text = ""
    for page in doc:
        raw_text += page.get_text()
    doc.close()

    # ---------------------------------------------

    # --- CHUNK 2 LOGIC: AI Analysis ---
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash", # Latest stable 2026 version
            contents=f"Extract professional details from this resume text: {raw_text}",
            config={
                "response_mime_type": "application/json",
                "response_schema": CandidateProfile, 
            }
        )
        
        # This converts the AI response directly into our Pydantic model
        profile_data = response.parsed
        
        return {
            "status": "success",
            "candidate": profile_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Processing failed: {str(e)}")
        