from fastapi import APIRouter, HTTPException
from app.models.story import StoryOutline, Story, StoryTemplate
from app.services.story_developer import StoryDeveloper
from app.services.exporter import Exporter
from app.services.illustrator import Illustrator
from app.services.version_control import VersionControl

from typing import List

router = APIRouter()

@router.post("/generate_outline")
async def generate_outline(input_data: dict) -> StoryOutline:
    try:
        return StoryDeveloper.generate_initial_outline(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/modify_outline")
async def modify_outline(outline: StoryOutline, modifications: dict) -> StoryOutline:
    try:
        return StoryDeveloper.modify_outline(outline, modifications)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/generate_story")
async def generate_story(outline: StoryOutline) -> Story:
    try:
        story = StoryDeveloper.generate_full_story(outline)
        return VersionControl.save_version(story)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/export_story/{story_id}")
async def export_story(story_id: str, format: str):
    try:
        story = StoryDeveloper.get_story(story_id)
        if format == "pdf":
            return Exporter.to_pdf(story)
        elif format == "epub":
            return Exporter.to_epub(story)
        else:
            raise HTTPException(status_code=400, detail="Unsupported format")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/generate_illustration/{chapter_id}")
async def generate_illustration(chapter_id: str):
    try:
        chapter = StoryDeveloper.get_chapter(chapter_id)
        return Illustrator.generate_illustration(chapter)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/story_versions/{story_id}")
async def get_story_versions(story_id: str) -> List[Story]:
    try:
        return VersionControl.get_versions(story_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/save_template")
async def save_template(template: StoryTemplate) -> StoryTemplate:
    try:
        return StoryDeveloper.save_template(template)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/templates")
async def get_templates() -> List[StoryTemplate]:
    try:
        return StoryDeveloper.get_templates()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))