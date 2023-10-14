import database
from entities import Base, UserEntity

# Reset Tables
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)

# Enter Mock Data
from sqlalchemy.orm import Session
session = Session(database.engine)

# TODO: Add a UserEntity to the database session and commit it.
grace = UserEntity(pid=730465719, first_name="Grace", last_name="Ku")
session.add(grace)
session.commit()