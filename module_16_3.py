from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(ge=5, le=20, description="Enter username", example="UrbanProfi")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="18")]) -> str:
    current_index = str(int(max(users, key=int))+1)
    message = f"Имя: {username}, возраст: {age}"
    users[current_index] = message
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, description="Inter user ID", example="1")],
                      username: Annotated[str, Path(ge=5, le=20, description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="18")]) -> str:
    message = f"Имя: {username}, возраст: {age}"
    users[user_id] = message
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description="Inter user ID", example="1")]) -> str:
    users.clear(user_id)
    return f"User {user_id} has been deleted"