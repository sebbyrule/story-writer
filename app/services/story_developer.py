from sqlalchemy.orm import Session
from app.models.database import Story, Character, Chapter
from app.models.story import StoryOutline, StoryInput
from app.services.character_developer import CharacterDeveloper
from app.utils.llm_singleton import LLMSingleton

class StoryDeveloper:
    def __init__(self, db: Session):
        self.db = db
        self.llm = LLMSingleton.get_instance()
        self.character_developer = CharacterDeveloper(db)

    def generate_initial_outline(self, story_input: StoryInput) -> StoryOutline:
        characters = self.character_developer.develop_all_characters(story_input.main_characters, story_input.genre)
        
        prompt = f"Create a chapter-by-chapter outline for a {story_input.genre} story titled '{story_input.title}' with the following plot points: {', '.join(story_input.plot_points)}"
        response = self.llm.invoke(prompt)
        
        # Parse the response to create chapters
        chapters = self._parse_chapter_outline(response)
        
        return StoryOutline(title=story_input.title, genre=story_input.genre, characters=characters, chapters=chapters)

    def _parse_chapter_outline(self, outline_text):
        # Implementation depends on the format of the LLM's response
        # This is a simplified version
        chapters = []
        for line in outline_text.split('\n'):
            if line.startswith("Chapter"):
                title, summary = line.split(': ', 1)
                chapters.append({"title": title, "summary": summary})
        return chapters

    def generate_full_story(self, outline: StoryOutline) -> Story:
        story = Story(title=outline.title, genre=outline.genre)
        self.db.add(story)
        self.db.commit()

        for char in outline.characters:
            db_char = Character(**char.dict(), story_id=story.id)
            self.db.add(db_char)

        full_content = ""
        for chapter_outline in outline.chapters:
            prompt = f"Write a full chapter for '{chapter_outline['title']}' with the following summary: {chapter_outline['summary']}"
            chapter_content = self.llm.invoke(prompt)
            
            db_chapter = Chapter(title=chapter_outline['title'], summary=chapter_outline['summary'], content=chapter_content, story_id=story.id)
            self.db.add(db_chapter)
            
            full_content += f"# {chapter_outline['title']}\n\n{chapter_content}\n\n"

        story.content = full_content
        self.db.commit()
        return story