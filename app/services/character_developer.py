from pydantic import BaseModel
from typing import List
from app.utils.llm_singleton import LLMSingleton
from app.core.config import settings
from app.core.logging_config import logger

class CharacterProfile(BaseModel):
    name: str
    background: str
    personality: str
    motivations: str
    physical_description: str

class CharacterDeveloper:
    def __init__(self):
        self.llm = LLMSingleton.get_instance()

    def develop_character(self, name: str, genre: str) -> CharacterProfile:
        prompt = f"Create a detailed character profile for {name} in a {genre} story. Include background, personality traits, motivations, and physical description."
        response = self.llm.invoke(prompt)
        
        # Parse the response into a CharacterProfile
        # This is a simplified parsing, you might need to adjust based on your LLM's output format
        lines = response.split('\n')
        return CharacterProfile(
            name=name,
            background=lines[0],
            personality=lines[1],
            motivations=lines[2],
            physical_description=lines[3]
        )

    def develop_all_characters(self, characters: List[str], genre: str) -> List[CharacterProfile]:
        return [self.develop_character(character, genre) for character in characters]