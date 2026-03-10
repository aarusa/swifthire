import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

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

# --------------- Sample Data ------------------------

userData = {
    1: {'id':'1', 'name':'user1'},
    2: {'id':'2', 'name':'user2'},
    3: {'id':'3', 'name':'user3'}
}

resumeData = {
    1: {'id':'1', 'name':'resume1'},
    2: {'id':'2', 'name':'resume2'},
    3: {'id':'3', 'name':'resume3'}
}

# --------------- Home Routes ------------------------
@app.get('/')
def read_root():
    return {'message': 'SwiftHire Backend is live.'}

# --------------- User Routes ------------------------
@app.get("/userList")
def getUserList():
    return userData

# --------------- Resume Routes ------------------------
@app.get("/resumeList")
def getResumeList():
    return resumeData

