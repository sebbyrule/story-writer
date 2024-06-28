import requests
from app.core.config import settings
from app.models.database import Chapter

class Illustrator:
    @staticmethod
    def generate_illustration(chapter: Chapter) -> str:
        prompt = f"Generate an illustration for a story chapter titled '{chapter.title}' with the following summary: {chapter.summary}"
        
        response = requests.post(
            settings.IMAGE_GENERATION_API_URL,
            headers={"Authorization": f"Bearer {settings.IMAGE_GENERATION_API_KEY}"},
            json={"prompt": prompt}
        )
        
        if response.status_code == 200:
            return response.json()['image_url']
        else:
            raise Exception(f"Failed to generate illustration: {response.text}")