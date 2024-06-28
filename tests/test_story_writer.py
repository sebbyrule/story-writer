import pytest
from fastapi.testclient import TestClient
from story_writer import app

client = TestClient(app)

def test_generate_story():
    story_input = {
        "title": "The Test Adventure",
        "genre": "Fantasy",
        "main_characters": ["Alice", "Bob"],
        "plot_points": ["Alice finds a magic key", "Bob discovers a hidden door"]
    }
    response = client.post("/generate_story", json=story_input)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "file_path" in response.json()

def test_generate_story_invalid_input():
    story_input = {
        "title": "",  # Invalid: empty title
        "genre": "Fantasy",
        "main_characters": ["Alice", "Bob"],
        "plot_points": ["Alice finds a magic key", "Bob discovers a hidden door"]
    }
    response = client.post("/generate_story", json=story_input)
    assert response.status_code == 400
