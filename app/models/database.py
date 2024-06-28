from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    stories = relationship("Story", back_populates="author")

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    version = Column(Integer, default=1)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="stories")
    characters = relationship("Character", back_populates="story")
    chapters = relationship("Chapter", back_populates="story")

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    background = Column(Text)
    personality = Column(Text)
    motivations = Column(Text)
    physical_description = Column(Text)
    story_id = Column(Integer, ForeignKey("stories.id"))
    story = relationship("Story", back_populates="characters")

class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    summary = Column(Text)
    content = Column(Text)
    story_id = Column(Integer, ForeignKey("stories.id"))
    story = relationship("Story", back_populates="chapters")
