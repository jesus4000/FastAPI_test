# uvicorn main2:app --reload --host=0.0.0.0 --port=8000

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


from typing import Optional
from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: Optional[str] = None


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    username = 'aa'
    password = 'bb'
    return templates.TemplateResponse("index.html", {"request": request, "username": username, "password":password})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user


@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    print('login', username, password)
    # return {"username": username, "password":password}
    return templates.TemplateResponse('index.html', context={'request': request, "username": username, "password":password})


# if __name__=="__main__":
#     uvicorn.run(app,host="0.0.0.0",port=8000)