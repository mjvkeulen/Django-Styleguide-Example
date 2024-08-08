from http import HTTPStatus

from django.contrib.auth import authenticate, login, logout
from ninja import Router, Schema
from ninja.security import django_auth
from ninja_jwt.authentication import JWTAuth
from rest_framework.response import Response

from bb.authentication.auth_objects import SessionAsHeaderAuthentication
from bb.core.schemas import ErrorSchema
from bb.users.api import UserOwnOutSchema
from bb.users.models import User

router = Router()


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


# TODO STACK: Settle on best approach to nest session and jwt routes into dedicated files with subrouters
# TODO STACK: Introduce an Auth mechanism that allows anonymous users to call this endpoint as well
@router.post("/session/login", response={200: LoginOutSchema, 400: ErrorSchema})
def authentication_session_login(request, data: LoginInSchema):
    user = authenticate(request, **data.dict())

    # TODO STACK: Match JWT behaviour
    if user is None:
        return HTTPStatus.BAD_REQUEST, {"message": "No active account found matching these credentials."}

    login(request, user)
    return HTTPStatus.OK, {"session": request.session.session_key, "data": request.user}


@router.api_operation(["GET", "POST"], "/session/logout")
def authentication_session_logout(request):
    logout(request)


# TODO STACK: Should also be compatible with JWT flow (so session is needed on top of token)
@router.get("/me", response=MeOutSchema, auth=[SessionAsHeaderAuthentication(), JWTAuth(), django_auth])
def authentication_me(request):
    return request.user
