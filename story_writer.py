from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import logging

from tools.markdown_writer import MarkdownWriter
from tools.chapter_writer import ChapterWriter
from tools.structured_output_handler import StructuredOutputHandler
from agents.story_agent import StoryAgent
from app.services.story_developer import InteractiveStoryDeveloper, StoryOutline
from app.core.config import settings
from exceptions import StoryWriterException
from app.core.logging_config import logger

app = FastAPI()

class StoryInput(BaseModel):
    title: str
    genre: str
    main_characters: List[str]
    plot_points: List[str]

class OutlineModification(BaseModel):
    modifications: Dict[str, str]

@app.post("/generate_story_outline")
async def generate_story_outline(story_input: StoryInput) -> StoryOutline:
    try:
        developer = InteractiveStoryDeveloper()
        outline = developer.generate_initial_outline(
            story_input.title,
            story_input.genre,
            story_input.main_characters,
            story_input.plot_points
        )
        logger.info(f"Generated initial outline for story: {story_input.title}")
        return outline
    except StoryWriterException as e:
        logger.error(f"Error generating story outline: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.post("/modify_story_outline")
async def modify_story_outline(outline: StoryOutline, modifications: OutlineModification) -> StoryOutline:
    try:
        developer = InteractiveStoryDeveloper()
        new_outline = developer.modify_outline(outline, modifications.modifications)
        logger.info(f"Modified outline for story: {outline.title}")
        return new_outline
    except StoryWriterException as e:
        logger.error(f"Error modifying story outline: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.post("/generate_full_story")
async def generate_full_story(outline: StoryOutline):
    try:
        story_agent = StoryAgent()
        structured_output = story_agent.create_structured_output(outline.dict())
        logger.info(f"Structured output created for story: {outline.title}")

        output_handler = StructuredOutputHandler()
        processed_output = output_handler.process_output(structured_output)
        logger.info(f"Processed output for story: {outline.title}")

        chapter_writer = ChapterWriter()
        full_story = ""
        for chapter in processed_output['chapters']:
            chapter_text = chapter_writer.write_chapter(chapter)
            full_story += chapter_text + "\n\n"
        logger.info(f"Full story written for: {outline.title}")

        markdown_writer = MarkdownWriter()
        file_path = markdown_writer.save_story_to_markdown(outline.title, full_story)
        logger.info(f"Story saved to file: {file_path}")

        return {"message": "Story generated successfully", "file_path": file_path}

    except StoryWriterException as e:
        logger.error(f"Error generating full story: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)