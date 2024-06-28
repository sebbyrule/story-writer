from langchain.prompts import PromptTemplate
from app.utils.llm_singleton import LLMSingleton

class ChapterWriter:
    def __init__(self):
        self.prompt_template = PromptTemplate(
            input_variables=["chapter_title", "summary"],
            template="Expand the following summary into a full chapter. Title: {chapter_title}. Summary: {summary}."
        )
        self.llm = LLMSingleton.get_instance()

    def write_chapter(self, chapter_info):
        """Takes the chapter info and returns the full text of the chapter."""
        # Debugging statements to check chapter_info
        print("Chapter info received:", chapter_info)
        
        # Ensure chapter_info is a dictionary with expected keys
        if not isinstance(chapter_info, dict) or 'chapter_title' not in chapter_info or 'summary' not in chapter_info:
            raise ValueError("Invalid chapter info format")

        # Format the input using the prompt template
        prompt = self.prompt_template.format(
            chapter_title=chapter_info['chapter_title'],
            summary=chapter_info['summary']
        )
        # Debugging statement to check formatted prompt
        print("Formatted prompt:", prompt)

        # Inovke the LLM with the formatted input
        chapter_text = self.llm.invoke(prompt)
        return chapter_text
