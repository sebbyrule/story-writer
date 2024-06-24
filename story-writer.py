from langchain_community.llms import Ollama
# from langchain_community.chains import LLMChain, PromptTemplate
from tools.markdown_writer import MarkdownWriter
from tools.chapter_writer import ChapterWriter
from tools.structured_output_handler import StructuredOutputHandler
from agents.story_agent import StoryAgent
from tools.input_handler import InputHandler

# llm = Ollama(
#     base_url='http://localhost:11434',
#     model='llama3',)

def main():
    try:
        # Get user input
        input_handler = InputHandler()
        user_input = input_handler.get_user_input()

        # Debugging statements to ensure user_input is correct
        print("User input:", user_input)

        # Extract the title from user_input
        title = user_input.get('title', 'untitled_story')

        # Debugging statements to ensure title is extracted correctly
        print("Title extracted:", title)

        # Create structured output
        story_agent = StoryAgent()
        try:
            structured_output = story_agent.create_structured_output(user_input)
            print("Structured output:", structured_output)
        except Exception as e:
            print("An error occurred while creating structured output:", e)
            return

        # Process structured output
        output_handler = StructuredOutputHandler()
        try:
            processed_output = output_handler.process_output(structured_output)
            print("Processed output:", processed_output)
        except Exception as e:
            print("An error occurred while processing the structured output:", e)
            return

        # Write chapters
        chapter_writer = ChapterWriter()
        full_story =  ""
        for chapter in processed_output['chapters']:
            # Debugging statements to ensure each chapter is processed correctly
            print("Processing chapter:", chapter)
            try:
                chapter_text = chapter_writer.write_chapter(chapter)
                full_story += chapter_text + "\n\n"
                print("Chapter text:", chapter_text)
            except Exception as e:
                print("An error occurred while writing a chapter:", e)

        # Save the story to Markdown
        try:
            markdown_writer = MarkdownWriter()
            markdown_writer.save_story_to_markdown(title, full_story)
        except Exception as e:
            print("An error occurred while saving the story to Markdown:", e)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()