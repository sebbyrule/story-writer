from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class Character(BaseModel):
    name: str
    background: str
    personality: str
    motivations: str
    physical_description: str

class Chapter(BaseModel):
    title: str
    summary: str
    content: Optional[str] = None

class StoryOutline(BaseModel):
    title: str
    genre: str
    characters: List[Character]
    chapters: List[Chapter]

class Story(BaseModel):
    id: str
    outline: StoryOutline
    full_content: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    version: int

class StoryTemplate(BaseModel):
    id: str
    name: str
    genre: str
    structure: List[Dict[str, str]]  # e.g. [{"chapter1": "Introduction"}, {"chapter2": "Rising Action"}]