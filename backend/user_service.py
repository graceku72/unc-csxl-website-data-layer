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
        # userEntity = UserEntity(pid=user.pid, first_name=user.first_name, last_name=user.last_name)
        # query = insert(UserEntity.from_model(UserEntity, user))
        # self._session.flush()
        #return user

        user_entity: UserEntity = UserEntity.from_model(user)
        self._session.add(user_entity)
        self._session.commit()
        return user_entity.to_model()


    def get(self, pid: int) -> User | None:
        #return self._session.execute(select(UserEntity).where(UserEntity.pid == pid))
        
        # user_entity = self._session.get(UserEntity, pid)
        # if user_entity:
        #     return user_entity.to_model() 
        # else:
        #     return None
        #     #raise ValueError("User cannot be found")

        query = select(UserEntity).where(UserEntity.pid == pid)
        entity = self._session.scalars(query).first()
        if entity:
            return entity.to_model()
        else:
            raise ValueError("User cannot be found")
    
    def delete(self, pid: int) -> None:
        query = select(UserEntity).where(UserEntity.pid == pid)
        entity = self._session.scalars(query).first()
        if entity:
            self._session.delete(entity)
            self._session.commit()
            # self._session.flush()
        else:
            raise ValueError("User cannot be found")