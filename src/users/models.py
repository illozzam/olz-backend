from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class UserBase(SQLModel):
    name: str
    email: str = Field(index=True)
    password: str


class User(UserBase, table=True):
    id: UUID = Field(primary_key=True, default=uuid4())
