class StructuredOutputHandler:
    def process_output(self, structured_output):
        """Wraps the structured output in a dictionary."""
        # Debugging statements to check structured output
        print("Structured output received:", structured_output)
        
        # Example processing (this should be customized based on actual structure)
        # Ensure structured_output is in the expected format
        if not isinstance(structured_output, dict) or 'chapters' not in structured_output:
            raise ValueError("Invalid structured output format")

        # Here you should have your processing logic
        # For simplicity, assuming structured_output contains a 'chapters' key with list of chapters
        processed_output = {'chapters': structured_output['chapters']}
        
        print("Processed output:", processed_output)
        return processed_output
