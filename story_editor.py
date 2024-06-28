from agents.editor_agent import EditorAgent

if __name__ == '__main__':
    agent = EditorAgent()
    edited_text = agent.edit_story("stories/sugar_rush.md")
    print(edited_text)