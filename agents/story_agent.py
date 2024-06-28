from langchain.prompts import PromptTemplate
from app.utils.llm_singleton import LLMSingleton
from app.services.character_developer import CharacterDeveloper
class StoryAgent:
    def __init__(self):
        self.prompt_template = PromptTemplate(
            input_variables=["title", "genre", "main_characters", "plot_points"],
            template="Create a structured story outline for a story titled '{title}' in the {genre} genre. The main characters are {main_characters}. The plot points are: {plot_points}. Provide a detailed chapter-by-chapter outline."
        )
        self.llm = LLMSingleton.get_instance()
        

    def create_structured_output(self, user_input):
        # Debugging statements to check user input
        print("User input received in create_structured_output:", user_input)

        # Format the input using the prompt template
        prompt = self.prompt_template.format(
            title=user_input['title'],
            genre=user_input['genre'],
            main_characters=user_input['main_characters'],
            plot_points=user_input['plot_points']
        )
        
        # Debugging statement to check formatted prompt
        print("Formatted prompt:", prompt)
        
        # Invoke the LLM with the formatted prompt
        structured_output = self.llm.invoke(prompt)
        
        # Debugging statement to check structured output
        print("Structured output returned:", structured_output)
        
        # Parse the structured output into a dictionary
        parsed_output = self.parse_structured_output(structured_output)
        
        return parsed_output

    def parse_structured_output(self, structured_output):
        # Parse the structured output from string to dictionary format
        chapters = structured_output.split("**Chapter")
        parsed_output = {"chapters": []}
        
        for chapter in chapters[1:]:  # Skip the first element as it's not a chapter
            chapter_title_end = chapter.find("**", 1)
            chapter_title = chapter[1:chapter_title_end].strip()
            chapter_content = chapter[chapter_title_end + 2:].strip()
            parsed_output["chapters"].append({
                "chapter_title": f"Chapter{chapter_title}",
                "summary": chapter_content
            })
        
        return parsed_output