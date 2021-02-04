from fastapi import FastAPI, Query
from pydantic import BaseModel


################################################################################
app = FastAPI()


################################################################################
class User(BaseModel):
    id: int
    name: str
    email: str


################################################################################
async def update_user(*, user: User):
    pass


################################################################################
async def get_user(*, user_id: int):
    u = User()
    u.id = user_id
    u.name = 'my name %d' % user_id
    u.email = 'my%d@a.b.c' % user_id
    return u


################################################################################
@app.get("/")
def read_root():
    return {"Hello": "World"}


################################################################################
@app.get('/user', response_model=User)
async def user(
    *,
    user_id: int = Query(..., title="The ID of the user to get", gt=0)
):
    # return {'user_id': user_id}
    my_user = get_user(user_id=user_id)
    return my_user


################################################################################
@app.post('/user/update', response_model=User)
async def update_user(
    *,
    user_id: int,
    really_update: int = Query(...)
):
    pass



################################################################################
@app.get("/search/{search_id}") # http://localhost:8000/search/1?q=test
def read_search(search_id: int, q: str = None):
    return {"search_id": search_id, "q": q}




################################################################################
# https://ichi.pro/ko/python-eseo-fastapi-sijaghagi-146061885479055
from fastapi import FastAPI, status, File, UploadFile

@app.post("/files/uploadfile", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):
    return {"message": " Valid file uploaded", "filetype": file.content_type}

# Uploading a pdf file
# API : http://localhost:8000/files/uploadfile



# uvicorn main:app --reload --host=0.0.0.0 --port=8000

