from app.models.story import Story
from typing import List
import uuid

class VersionControl:
    @staticmethod
    def save_version(story: Story) -> Story:
        # In a real implementation, this would save to a database
        story.version += 1
        story.id = str(uuid.uuid4())  # Generate a new ID for each version
        return story

    @staticmethod
    def get_versions(story_id: str) -> List[Story]:
        # In a real implementation, this would fetch from a database
        # For now, we'll return a dummy list
        return [Story(id=story_id, version=1), Story(id=story_id, version=2)]