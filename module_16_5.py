from fastapi import FastAPI, Path, HTTPException, Request, status, Body
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    for us_id in users:
        if us_id != user_id:
            raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})


@app.post("/user/{username}/{age}")
async def post_user(
                    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Urban")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="18")]) -> User:
        user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
        user = User(id=user_id, username=username, age=age)
        users.append(user)
        return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Urban")],
                      user_id: int = Path(ge=1, description="Inter user ID", example="1"),
                      age: int = Path(ge=18, le=120, description="Enter age", example="18")) -> User:
    for inter_user in users:
        if inter_user.id == user_id:
           inter_user.username = username
           inter_user.age = age
           return inter_user
        raise HTTPException(status_code=404, detail="User was not found, code 404")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=1, description="Inter user ID", example="1")) -> User:
    for exit_user in users:
        if exit_user.id == user_id:
            users.remove(exit_user)
            return exit_user
    raise HTTPException(status_code=404, detail="User not found")