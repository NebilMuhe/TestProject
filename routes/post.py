from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import post as post_schemas, user as user_schemas
from services import post_service
from dependencies.auth import get_current_user
from database import get_db
from utils.cache import get_cached_posts, set_cached_posts

router = APIRouter()

@router.post("/posts", response_model=post_schemas.PostInDB)
def add_post(post: post_schemas.PostCreate, current_user: user_schemas.UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    db_post = post_service.create_post(db, post, current_user.id)
    return db_post

@router.get("/posts", response_model=list[post_schemas.PostInDB])
def get_posts(current_user: user_schemas.UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    cached_posts = get_cached_posts(current_user.id)
    if cached_posts:
        return cached_posts
    db_posts = post_service.get_posts(db, current_user.id)
    set_cached_posts(current_user.id, db_posts)
    return db_posts

@router.delete("/posts/{post_id}", response_model=post_schemas.PostInDB)
def delete_post(post_id: int, current_user: user_schemas.UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    db_post = post_service.delete_post(db, post_id, current_user.id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
