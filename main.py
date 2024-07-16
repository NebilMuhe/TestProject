from fastapi import FastAPI
from database import engine, Base
from routes import auth, post
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(post.router, prefix="/post", tags=["post"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)