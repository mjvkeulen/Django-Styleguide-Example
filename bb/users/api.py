from ninja import Router
from ninja import Schema
from ninja_jwt.authentication import JWTAuth
from bb.users.models import User

router = Router()


class UserOwnOutSchema(Schema):
    id: int
    username: str


class UserOutSchema(Schema):
    id: int
    username: str


@router.get("/{pk}", response=UserOutSchema, auth=JWTAuth())
def user_get(request, pk: int):
    """Placeholder"""
    user = User.objects.get(pk=pk)
    return user
