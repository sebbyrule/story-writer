from langchain_community.llms import Ollama

class LLMSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if LLMSingleton._instance is None:
            LLMSingleton._instance = Ollama(
                base_url='http://localhost:11434',
                model='llama3',
            )
        return LLMSingleton._instance