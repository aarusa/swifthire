import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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

# --------------- Sample Data ------------------------
# Should i use dictionaries inside a list or dictionaries inside a dictionary for data???
# User Data
userData = [
    {
        "user_id": 101,
        "username": "jsmith_dev",
        "first_name": "Jordan",
        "last_name": "Smith",
        "email": "j.smith88@example.com",
        "location": "New York, USA",
        "account_tier": "Premium",
        "last_login": "2026-03-09",
        "is_active": True
    },
    {
        "user_id": 102,
        "username": "elena_stats",
        "first_name": "Elena",
        "last_name": "Rodriguez",
        "email": "elena.rod@example.com",
        "location": "Madrid, Spain",
        "account_tier": "Free",
        "last_login": "2026-03-10",
        "is_active": True
    },
    {
        "user_id": 103,
        "username": "mchen_pixel",
        "first_name": "Marcus",
        "last_name": "Chen",
        "email": "mchen_design@example.com",
        "location": "Toronto, Canada",
        "account_tier": "Premium",
        "last_login": "2026-02-28",
        "is_active": True
    },
    {
        "user_id": 104,
        "username": "s_jenkins_mkt",
        "first_name": "Sarah",
        "last_name": "Jenkins",
        "email": "sjenks_mkt@example.com",
        "location": "London, UK",
        "account_tier": "Enterprise",
        "last_login": "2026-03-05",
        "is_active": False
    },
    {
        "user_id": 105,
        "username": "d_okafor_fin",
        "first_name": "David",
        "last_name": "Okafor",
        "email": "dokafor_finance@example.com",
        "location": "Lagos, Nigeria",
        "account_tier": "Free",
        "last_login": "2026-03-01",
        "is_active": True
    },
    {
        "user_id": 106,
        "username": "amelia_v_pm",
        "first_name": "Amelia",
        "last_name": "Vasseur",
        "email": "amelia.v@example.com",
        "location": "Paris, France",
        "account_tier": "Premium",
        "last_login": "2026-03-08",
        "is_active": True
    },
    {
        "user_id": 107,
        "username": "liam_infra",
        "first_name": "Liam",
        "last_name": "O'Connor",
        "email": "liam.oc@example.com",
        "location": "Dublin, Ireland",
        "account_tier": "Enterprise",
        "last_login": "2026-03-10",
        "is_active": True
    },
    {
        "user_id": 108,
        "username": "mpatel_people",
        "first_name": "Maya",
        "last_name": "Patel",
        "email": "mpatel_hr@example.com",
        "location": "Mumbai, India",
        "account_tier": "Free",
        "last_login": "2026-01-15",
        "is_active": False
    },
    {
        "user_id": 109,
        "username": "jwilson_sales",
        "first_name": "James",
        "last_name": "Wilson",
        "email": "jwilson_sales@example.com",
        "location": "Chicago, USA",
        "account_tier": "Premium",
        "last_login": "2026-03-07",
        "is_active": True
    },
    {
        "user_id": 110,
        "username": "chloe_codes",
        "first_name": "Chloe",
        "last_name": "Zhao",
        "email": "czhao.dev@example.com",
        "location": "Singapore",
        "account_tier": "Free",
        "last_login": "2026-03-09",
        "is_active": True
    },
    {
        "user_id": 111,
        "username": "rob_secure",
        "first_name": "Robert",
        "last_name": "Miller",
        "email": "rmiller_security@example.com",
        "location": "Berlin, Germany",
        "account_tier": "Enterprise",
        "last_login": "2026-03-03",
        "is_active": True
    },
    {
        "user_id": 112,
        "username": "sophia_art",
        "first_name": "Sophia",
        "last_name": "Rossi",
        "email": "srossi_creative@example.com",
        "location": "Rome, Italy",
        "account_tier": "Premium",
        "last_login": "2026-03-04",
        "is_active": True
    },
    {
        "user_id": 113,
        "username": "kd_backend",
        "first_name": "Kevin",
        "last_name": "Durant",
        "email": "kdurant.dev@example.com",
        "location": "San Francisco, USA",
        "account_tier": "Free",
        "last_login": "2026-03-09",
        "is_active": True
    },
    {
        "user_id": 114,
        "username": "bella_garcia",
        "first_name": "Isabella",
        "last_name": "Garcia",
        "email": "igarcia_cs@example.com",
        "location": "Mexico City, Mexico",
        "account_tier": "Premium",
        "last_login": "2026-03-01",
        "is_active": True
    },
    {
        "user_id": 115,
        "username": "tom_sysadmin",
        "first_name": "Thomas",
        "last_name": "Wright",
        "email": "twright_admin@example.com",
        "location": "Sydney, Australia",
        "account_tier": "Free",
        "last_login": "2025-12-25",
        "is_active": False
    },
    {
        "user_id": 116,
        "username": "fatima_po",
        "first_name": "Fatima",
        "last_name": "Al-Sayed",
        "email": "fatima.as@example.com",
        "location": "Dubai, UAE",
        "account_tier": "Enterprise",
        "last_login": "2026-03-10",
        "is_active": True
    },
    {
        "user_id": 117,
        "username": "oliver_qa",
        "first_name": "Oliver",
        "last_name": "Twist",
        "email": "otwist_qa@example.com",
        "location": "London, UK",
        "account_tier": "Free",
        "last_login": "2026-03-06",
        "is_active": True
    },
    {
        "user_id": 118,
        "username": "grace_ml",
        "first_name": "Grace",
        "last_name": "Hopper",
        "email": "ghopper_ml@example.com",
        "location": "Boston, USA",
        "account_tier": "Premium",
        "last_login": "2026-03-10",
        "is_active": True
    },
    {
        "user_id": 119,
        "username": "noah_logistics",
        "first_name": "Noah",
        "last_name": "Williams",
        "email": "nwilliams_logistics@example.com",
        "location": "Amsterdam, Netherlands",
        "account_tier": "Free",
        "last_login": "2026-02-14",
        "is_active": True
    },
    {
        "user_id": 120,
        "username": "zoe_social",
        "first_name": "Zoe",
        "last_name": "Kravitz",
        "email": "zkravitz_social@example.com",
        "location": "Los Angeles, USA",
        "account_tier": "Premium",
        "last_login": "2026-03-09",
        "is_active": True
    }
]

# Resume Data
resumeData = [
    {
        "resume_id": 1,
        "user_id": 101,
        "first_name": "Jordan",
        "last_name": "Smith",
        "job_title": "Senior Software Engineer",
        "years_experience": 8,
        "skills": ["Python", "AWS", "Docker", "Kubernetes"],
        "education": "B.S. Computer Science"
    },
    {
        "resume_id": 2,
        "user_id": 102,
        "first_name": "Elena",
        "last_name": "Rodriguez",
        "job_title": "Data Scientist",
        "years_experience": 4,
        "skills": ["R", "TensorFlow", "SQL", "Pandas"],
        "education": "M.S. Applied Statistics"
    },
    {
        "resume_id": 3,
        "user_id": 103,
        "first_name": "Marcus",
        "last_name": "Chen",
        "job_title": "UX Designer",
        "years_experience": 6,
        "skills": ["Figma", "Adobe XD", "User Research", "Prototyping"],
        "education": "B.F.A. Graphic Design"
    },
    {
        "resume_id": 4,
        "user_id": 104,
        "first_name": "Sarah",
        "last_name": "Jenkins",
        "job_title": "Marketing Manager",
        "years_experience": 10,
        "skills": ["SEO", "Google Analytics", "Content Strategy", "HubSpot"],
        "education": "B.A. Communications"
    },
    {
        "resume_id": 5,
        "user_id": 105,
        "first_name": "David",
        "last_name": "Okafor",
        "job_title": "Financial Analyst",
        "years_experience": 3,
        "skills": ["Excel VBA", "Financial Modeling", "Bloomberg", "SAP"],
        "education": "B.S. Finance"
    },
    {
        "resume_id": 6,
        "user_id": 106,
        "first_name": "Amelia",
        "last_name": "Vasseur",
        "job_title": "Project Manager",
        "years_experience": 7,
        "skills": ["Agile", "Scrum", "Jira", "Risk Management"],
        "education": "MBA"
    },
    {
        "resume_id": 7,
        "user_id": 107,
        "first_name": "Liam",
        "last_name": "O'Connor",
        "job_title": "DevOps Engineer",
        "years_experience": 5,
        "skills": ["Terraform", "Jenkins", "Linux", "Ansible"],
        "education": "B.S. Information Technology"
    },
    {
        "resume_id": 8,
        "user_id": 108,
        "first_name": "Maya",
        "last_name": "Patel",
        "job_title": "HR Specialist",
        "years_experience": 4,
        "skills": ["Recruiting", "Employee Relations", "Workday", "Onboarding"],
        "education": "B.A. Psychology"
    },
    {
        "resume_id": 9,
        "user_id": 109,
        "first_name": "James",
        "last_name": "Wilson",
        "job_title": "Sales Executive",
        "years_experience": 12,
        "skills": ["CRM", "Negotiation", "B2B Sales", "Lead Generation"],
        "education": "B.S. Business Admin"
    },
    {
        "resume_id": 10,
        "user_id": 110,
        "first_name": "Chloe",
        "last_name": "Zhao",
        "job_title": "Frontend Developer",
        "years_experience": 2,
        "skills": ["React", "TypeScript", "CSS3", "Next.js"],
        "education": "Self-Taught / Bootcamp"
    },
    {
        "resume_id": 11,
        "user_id": 111,
        "first_name": "Robert",
        "last_name": "Miller",
        "job_title": "Cybersecurity Analyst",
        "years_experience": 6,
        "skills": ["Penetration Testing", "Wireshark", "SIEM", "Python"],
        "education": "B.S. Cybersecurity"
    },
    {
        "resume_id": 12,
        "user_id": 112,
        "first_name": "Sophia",
        "last_name": "Rossi",
        "job_title": "Art Director",
        "years_experience": 9,
        "skills": ["Creative Direction", "Illustrator", "Branding", "Team Leadership"],
        "education": "M.A. Visual Arts"
    },
    {
        "resume_id": 13,
        "user_id": 113,
        "first_name": "Kevin",
        "last_name": "Durant",
        "job_title": "Backend Developer",
        "years_experience": 4,
        "skills": ["Go", "PostgreSQL", "Microservices", "Redis"],
        "education": "B.S. Computer Engineering"
    },
    {
        "resume_id": 14,
        "user_id": 114,
        "first_name": "Isabella",
        "last_name": "Garcia",
        "job_title": "Customer Success Lead",
        "years_experience": 5,
        "skills": ["Zendesk", "Account Management", "Churn Reduction", "Salesforce"],
        "education": "B.A. Sociology"
    },
    {
        "resume_id": 15,
        "user_id": 115,
        "first_name": "Thomas",
        "last_name": "Wright",
        "job_title": "Systems Administrator",
        "years_experience": 15,
        "skills": ["Active Directory", "VMware", "Networking", "PowerShell"],
        "education": "Associate Degree in IT"
    },
    {
        "resume_id": 16,
        "user_id": 116,
        "first_name": "Fatima",
        "last_name": "Al-Sayed",
        "job_title": "Product Owner",
        "years_experience": 6,
        "skills": ["Roadmapping", "Backlog Grooming", "Stakeholder Mgmt", "Kanban"],
        "education": "B.S. Management Information Systems"
    },
    {
        "resume_id": 17,
        "user_id": 117,
        "first_name": "Oliver",
        "last_name": "Twist",
        "job_title": "QA Automation Engineer",
        "years_experience": 3,
        "skills": ["Selenium", "PyTest", "Cypress", "CI/CD"],
        "education": "B.S. Software Engineering"
    },
    {
        "resume_id": 18,
        "user_id": 118,
        "first_name": "Grace",
        "last_name": "Hopper",
        "job_title": "Machine Learning Engineer",
        "years_experience": 2,
        "skills": ["PyTorch", "NLP", "Scikit-Learn", "Matplotlib"],
        "education": "Ph.D. Computer Science"
    },
    {
        "resume_id": 19,
        "user_id": 119,
        "first_name": "Noah",
        "last_name": "Williams",
        "job_title": "Supply Chain Planner",
        "years_experience": 8,
        "skills": ["Logistics", "Inventory Mgmt", "ERP Systems", "Forecasting"],
        "education": "B.S. Supply Chain Management"
    },
    {
        "resume_id": 20,
        "user_id": 120,
        "first_name": "Zoe",
        "last_name": "Kravitz",
        "job_title": "Social Media Strategist",
        "years_experience": 4,
        "skills": ["TikTok Analytics", "Copywriting", "Influencer Outreach", "CapCut"],
        "education": "B.A. Marketing"
    }
]
    
# --------------- Home Routes ------------------------
@app.get('/')
def home():
    return {'message': 'SwiftHire Backend is live.'}

# --------------- User Routes ------------------------
# Displaying user list
@app.get("/user/list")
def get_user_list():
    return userData

# Displaying single user based on id
@app.get("/user/{id}")
def get_user_by_id(id:int):
    return userData[id]

# Adding a new user
@app.post("/users/add")
async def add_user(new_user: schemas.User):
    # 1. Convert the incoming Pydantic model to a Python Dictionary
    user_dict = new_user.model_dump()
    
    # 2. Check if the user_id already exists to prevent duplicates
    if any(u['user_id'] == user_dict['user_id'] for u in userData):
        raise HTTPException(status_code=400, detail="User ID already exists")

    # 3. Add the dictionary to your list
    userData.append(user_dict)
    
    return {"message": "User added successfully", "data": user_dict}

# --------------- Resume Routes ------------------------
# Displaying resume list
@app.get("/resume/list")
def get_resume_list():
    return resumeData

# Displaying single resume based on id
@app.get("/resume/{id}")
def get_resume_by_id(id:int):
    return resumeData[id]

# Adding a new resume
@app.post("/resume/add")
async def add_resume(new_resume: schemas.Resume):
    resume_dict = new_resume.model_dump()

    if any(r['resume_id'] == resume_dict['resume_id'] for r in resumeData):
        raise HTTPException(status_code=400, detail="Resume already exists")
        
    resumeData.append(resume_dict)

    return {"message": "Resume added successfully", "data": resume_dict}



