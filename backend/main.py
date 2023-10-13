from fastapi import FastAPI, Depends
from user_service import UserService, User

app = FastAPI()

@app.get("/api/users")
def get_users(user_service: UserService = Depends()) -> list[User]:
    return user_service.all()


@app.post("/api/users")
def new_user(user: User, user_service: UserService = Depends()) -> User:
    raise NotImplemented()


@app.get("/api/users/{pid}", responses={404: {"model": None}})
def get_user(pid: int, user_service: UserService = Depends()) -> User:
    raise NotImplemented()


@app.delete("/api/users/{pid}")
def delete_user(pid: int, user_service = Depends(UserService)):
    raise NotImplemented()