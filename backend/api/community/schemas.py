from ninja import Schema
from datetime import date
from typing import Literal

class CreateCommunityInput(Schema):
    name: str
    description: str
    type_community: Literal['temporary', 'continuous']

class UserSummary(Schema):
    id: int
    username: str

class CreateCommunityOutput(Schema):
    id: int
    name: str
    description: str
    type_community: Literal['temporary', 'continuous']
    create_at: date
    creator: UserSummary