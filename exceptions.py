class StoryWriterException(Exception):
    """Base exception for StoryWriter application"""

class InvalidInputError(StoryWriterException):
    """Raised when input is invalid"""

class LLMError(StoryWriterException):
    """Raised when there's an error with the LLM"""

class FileOperationError(StoryWriterException):
    """Raised when there's an error with file operations"""