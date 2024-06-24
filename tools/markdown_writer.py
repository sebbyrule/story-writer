import os

class MarkdownWriter:
    def save_story_to_markdown(self, title, story):
        # Ensure the output directory exists
        output_dir = "stories"
        os.makedirs(output_dir, exist_ok=True)
        
        # Debugging statements to check the inputs
        print("Title type:", type(title))
        print("Title:", title)
        print("Story type:", type(story))
        print("Story:", story)

        # Create a markdown file with the story title
        filename = f"{output_dir}/{title.replace(' ', '_').lower()}.md"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"# {title}\n\n")
                file.write(story)
            print(f"Story saved to {filename}")
        except Exception as e:
            print("Error writing to markdown file:", e)
            raise
