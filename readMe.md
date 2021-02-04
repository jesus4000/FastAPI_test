fastAPI reference
=================


## 참조 사이트

<https://fastapi.tiangolo.com/tutorial/first-steps/>

<https://phrase.com/blog/posts/fastapi-i18n/>

---

## auto api manual
```
localhost:8000/docs
```
```
localhost:8000/redoc
```

---


## 기본 사용

### 사전설치 package
```
pip install fastapi
pip install uvicorn
pip install jinja2
pip install aiofiles
```

### fastAPI 서버 실행
```
uvicorn main:app --reload --host=0.0.0.0 --port=8000
```
##### Inline python directed run
```
import uvicorn

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
```

### library 구성
```
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI() # `app` 이름이 main:app 에 쓰이는 항목임 

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
```

#### 단순 json 출력
```
@app.get("/")
async def root():
    return {"message": "Hello World"}
```
#### html request 출력
```
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
```

#### return List
```
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item
```
---

## HTML for fastAPI

#### 일반 주소는 get 방식으로 받고, post 방식으로 form 처리 action 지정
```
# form In
@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# form submit out
@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = str(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})
```

#### form 사용시 구문
```
# form submit out
def method_name(request: Request, variable_name: str = Form(...)):
    print(variable_name) # webpage in {{ variable_name }}
    return templates.TemplateResponse('render_page.html', context={'request': request, 'variable_name': variable_name})
```
##### 반드시 name 값을 위의 변수로 지정필요
```
<form method="post">
    <input type="number" **name="variable_name"** value="1234"/>
    <input type="submit">
</form>
```


---


## 기타 사용관련

#### Enum 사용
```
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}    
```
