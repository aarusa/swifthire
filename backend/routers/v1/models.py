from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class JobModel(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    required_skills = Column(JSON) # SQLite can store lists as JSON!
    min_years_experience = Column(Integer)
    description_text = Column(String)