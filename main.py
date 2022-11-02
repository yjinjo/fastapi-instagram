from fastapi import FastAPI, HTTPException
from starlette.responses import PlainTextResponse

from exceptions import StoryException
from router import blog_get
from router import blog_post
from router import user
from router import article
from db import models
from db.database import engine
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return {'message': 'Hello world!'}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)
