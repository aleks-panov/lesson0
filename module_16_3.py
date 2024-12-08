from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Urban")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="18")]) -> str:
    current_index = str(int(max(users, key=int))+1)
    message = f"Имя: {username}, возраст: {age}"
    users[current_index] = message
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Urban")],
                      user_id: int = Path(ge=1, description="Inter user ID", example="1"),
                      age: int = Path(ge=18, le=120, description="Enter age", example="18")) -> dict:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"The user {user_id} is updated"}


@app.delete("/user/{user_id}")
async def delete_user(user_id: str = Path(min_length=1, description="Inter user ID", example="1")) -> dict:
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}