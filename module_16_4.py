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
    return f"id {user.id}, username {user.username}, age {user.age}"


@app.put("/user/{user_id}/{username}/{age}", response_model=str)
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Urban")],
                      user_id: int = Path(ge=1, description="Inter user ID", example="1"),
                      age: int = Path(ge=18, le=120, description="Enter age", example="18")) -> str:
    for inter_user in users:
        if inter_user.id == user_id:
           inter_user.username = username
           inter_user.age = age
           return f"id {inter_user.id}, username {inter_user.username}, age {inter_user.age}"
        else:
            HTTPException(status_code=404, detail="User was not found, code 404")


@app.delete("/user/{user_id}", response_model=str)
async def delete_user(user_id: int = Path(ge=1, description="Inter user ID", example="1")) -> str:
    for index, exit_user in enumerate(users):
        if exit_user.id == user_id:
            users.pop(index)
            return f"id {exit_user.id}, username {exit_user.username}, age {exit_user.age}"

    raise HTTPException(status_code=404, detail="User not found")