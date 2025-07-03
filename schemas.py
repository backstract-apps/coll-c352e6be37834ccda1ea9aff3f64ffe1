from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    id: Any
    name: str
    login_details: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    login_details: str
    class Config:
        from_attributes = True


class Todos(BaseModel):
    id: Any
    description: str
    completed: int
    user_id: int


class ReadTodos(BaseModel):
    id: Any
    description: str
    completed: int
    user_id: int
    class Config:
        from_attributes = True


