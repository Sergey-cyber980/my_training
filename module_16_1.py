from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    age: int

@app.get("/")
async def main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_login():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_login(user_id: int = Path(..., title="ID пользователя", ge=1)):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user_info(user: User):
    return {"message": f"Информация о пользователе. Имя: {user.username}, Возраст: {user.age}"}
