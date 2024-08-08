from ninja import Router

from bb.users.models import User

from .schemas import UserOtherOutSchema

router = Router()


@router.get("/{pk}", response=UserOtherOutSchema)
def user_get(request, pk: int):
    """Placeholder"""
    return User.objects.get(pk=pk)
