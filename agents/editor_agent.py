from langchain.text_splitter import MarkdownTextSplitter, RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from app.utils.llm_singleton import LLMSingleton
class EditorAgent:
    def __init__(self):
        self.llm = LLMSingleton.get_instance()
        self.text_splitter = MarkdownTextSplitter(chunk_size=2500, chunk_overlap=200, length_function=len)
        self.edit_prompt = PromptTemplate(
            input_variables=["chunk"],
            template="You are an expert editor. Review and improve the following text:\n\n{chunk}\n\nProvide the edited version:"
           )

    def read_markdown(self, file_path):
        with open(file_path, 'r') as file:
            print(f"Reading file: {file_path}")
            return file.read()

    def chunk_text(self, text):
        print(f"Chunking text: {text}")
        return self.text_splitter.split_text(text)

    def edit_chunk(self, chunk):
        print(f"Envoking LLM: {chunk}")
        prompt = self.edit_prompt.format(chunk=chunk)
        return self.llm.invoke(prompt)

    def recursive_edit(self, chunks, depth=0, max_depth=1):
        if depth >= max_depth:
            print("returning chunk")
            return chunks

        edited_chunks = [self.edit_chunk(chunk) for chunk in chunks]
        print(f"Edited chunks: {edited_chunks}")
        return self.recursive_edit(edited_chunks, depth + 1, max_depth)

    def edit_story(self, file_path):
        original_text = self.read_markdown(file_path)
        chunks = self.chunk_text(original_text)
        edited_chunks = self.recursive_edit(chunks)
        return "\n\n".join(edited_chunks)
   
if __name__ == "__main__":
    agent = EditorAgent()
    edited_text = agent.edit_story("../stories/my_dad_farts.md")
    print(edited_text)