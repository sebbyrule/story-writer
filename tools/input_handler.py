class InputHandler:
    def get_user_input(self):
        """Used to get structured user input for the start of the chain."""
        title = input("Enter the title of your story: ").strip()
        genre = input("Enter the genre of your story: ").strip()
        main_characters = input("Enter the main characters (comma-separated): ").strip()
        plot_points = input("Enter the main plot points (semicolon-separated): ").strip()

        # Basic validation
        if not title or not genre or not main_characters or not plot_points:
            raise ValueError("All fields are required and cannot be empty.")
        
        return {
            "title": title,
            "genre": genre,
            "main_characters": main_characters,
            "plot_points": plot_points
        }
