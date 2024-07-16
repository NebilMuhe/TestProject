from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.post import Post
from models.user import User
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

User.metadata.create_all(bind=engine)
Post.metadata.create_all(bind=engine)
