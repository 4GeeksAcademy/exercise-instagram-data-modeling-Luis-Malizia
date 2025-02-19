import os
import sys
import enum
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey,Table, Column, Enum
from eralchemy2 import render_er
from typing import List

Base = declarative_base()

Follower = Table(
    "follower",
    Base.metadata,
    Column("user_from_id", ForeignKey("user.id")),
    Column("user_to_id", ForeignKey("user.id")),
)

class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False)
    comment: Mapped[List["Comment"]] = relationship()
    
class Post(Base):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    
class Comment(Base):
     __tablename__ = 'comment'
     id: Mapped[int] = mapped_column(primary_key=True)
     comment_text: Mapped[str] = mapped_column(String(500), nullable=False)
     author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
     post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[MyEnum] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[str] = mapped_column(ForeignKey("post.id"))

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
