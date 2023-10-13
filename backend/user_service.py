from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import db_session
from models import User
from entities import UserEntity


class UserService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[User]:
        query = select(UserEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def create(self, user: User) -> User:
        # TODO
        raise NotImplemented()

    def get(self, pid: int) -> User | None:
        # TODO
        raise NotImplemented()

    def delete(self, pid: int) -> None:
        # TODO
        raise NotImplemented()