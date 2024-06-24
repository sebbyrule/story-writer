from pydantic import BaseModel, Field
from typing import List

class UserInput(BaseModel):
    title: str = Field(..., example="The Great Adventure")
    genre: str = Field(..., example="Fantasy")
    main_characters: List[str] = Field(..., example=["Alice", "Bob"])
    plot_points: List[str] = Field(..., example=["Alice discovers a secret portal", "Bob gets kidnapped by a dragon"])
