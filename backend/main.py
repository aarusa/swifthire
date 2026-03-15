import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes import user_routes, resume_routes
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
   
# --------------- Home Routes ------------------------
@app.get('/')
def home():
    return {'message': 'SwiftHire Backend is live.'}

# Register route modules
app.include_router(user_routes.router, prefix="/user", tags=["Users"])
app.include_router(resume_routes.router, prefix="/resume", tags=["Resumes"])
