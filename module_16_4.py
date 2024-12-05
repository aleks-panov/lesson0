from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def post_user(user: User,
                    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Urban")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="18")]) -> str:
    if users:
        current_index = max(user.id for user in users) + 1
    else:
        current_index = 1
    user.id = current_index
    user.username = username
    user.age = age
    users.append(user)
    return f"User {current_index} is registreted"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, description="Inter user ID", example="1")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Urban")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="18")]) -> str:
    for inter_user in users:
        if inter_user.id == user_id:
           inter_user.username = username
           inter_user.age = age
           return f"User {inter_user.id} is updated"
        else:
            HTTPException(status_code=404, detail="User was not found, code 404")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description="Inter user ID", example="Urban")]):
    for exit_user in users:
        if exit_user.id == user_id:
            del users[user_id]
            return f"User {exit_user.id} has been deleted"
        else:
            HTTPException(status_code=404, detail="User not found")