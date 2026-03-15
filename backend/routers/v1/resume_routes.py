from fastapi import APIRouter, HTTPException
import schemas
from data.resumes import resumeData

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

