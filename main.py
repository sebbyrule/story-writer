from fastapi import FastAPI
from app.api import story, auth

app = FastAPI()

app.include_router(story.router, prefix="/api/story", tags=["story"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)