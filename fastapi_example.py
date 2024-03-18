from fastapi import FastAPI
from pydantic import BaseModel

# аннотации типов
# класс с типами данных параметров 
class Item(BaseModel):
    name: str
    description: str
    price: float
item = Item(name="Это тестовая строка",description="test",price=100)
print(item.name)

# создаем объект приложения
app = FastAPI()

# функция, которая будет обрабатывать запрос по пути "/"
# полный путь запроса http://127.0.0.1:8000/
@app.get("/")
def root():
    return {"message": "Hello FastAPI_1"}

# функция, которая обрабатывает запрос по пути "/about"
@app.get("/about")
def about():
    return {"message": "Страница с описанием проекта"}

# функция-обработчик с параметрами пути
@app.get("/users/{id}")
def users(id):
    return {"user_id": id}

@app.get("/users")
def get_model(item):
    return {"user_name": item.name, "description": item.description, "price": item.price}

@app.get("/text={params}")
def get_text(params):
    return {"params": params}


# функция-обработчик post запроса с параметрами
#@app.post("/users")
#def post_model(item:Item):
#    return {"user_name": item.name, "description": item.description, "price": item.price}

