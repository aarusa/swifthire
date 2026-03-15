import uvicorn
from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routers import user_routes, resume_routes
from pydantic import BaseModel
from typing import List
import schemas

app = FastAPI()

origins = [
    # All routes
    "http://localhost:3000"
]

# Implement CORS middlewaare, prohibits unauthorised websites, endpoints, or servers from accessing API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
   
# ------------ System Routes --------------
@app.get('/')
def home():
    return {
        "status": "online",
        "message": "SwiftHire Backend is live",
        "version": "v1"
    }

# ------------ API Versioning --------------
api_v1 = APIRouter()

# ------------ Registering API Routes --------------
api_v1.include_router(user_routes.router, prefix="/user", tags=["Users"])
api_v1.include_router(resume_routes.router, prefix="/resume", tags=["Resumes"])

app.include_router(api_v1, prefix="/api/v1")
