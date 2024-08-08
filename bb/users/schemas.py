from ninja import Schema


class UserOwnOutSchema(Schema):
    id: int
    username: str


class UserOtherOutSchema(Schema):
    id: int
    username: str
