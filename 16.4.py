from fastapi import FastAPI, Path, HTTPException, Body
from typing import Annotated, List

from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5,
                                                    max_length=20,
                                                    description="Enter username",
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description="Enter age",
                                               example=25)]):
    user_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(gt=0)],
                      username: Annotated[str, Path(min_length=5,
                                                    max_length=20,
                                                    description="Enter username",
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description="Enter age",
                                               example=25)]):
    try:
            users[user_id-1] = User(id=user_id, username=username, age=age)
            return users[user_id-1]
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id-1)
        return users.pop(user_id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
