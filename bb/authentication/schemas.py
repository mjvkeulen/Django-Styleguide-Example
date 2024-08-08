from ninja import Schema

from bb.users.schemas import UserOwnOutSchema


class LoginInSchema(Schema):
    password: str
    username: str


class LoginOutSchema(Schema):
    session: str
    data: UserOwnOutSchema


class MeOutSchema(Schema):
    username: str
    is_authenticated: bool
    # Unauthenticated users don't have the following fields, so provide defaults.
    email: str = None
    full_name: str = None
