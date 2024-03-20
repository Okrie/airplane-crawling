from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 메인
@app.post('/', status_code=201)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request' : request})