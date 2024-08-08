from importlib import import_module
from typing import TYPE_CHECKING, Any, Optional, Sequence, Type

from django.conf import settings
from django.contrib import auth
from django.http import HttpRequest
from ninja.security import HttpBearer, django_auth
from ninja_jwt.authentication import JWTAuth


class SessionAsHeaderAuthentication(HttpBearer):
    """
    In case we are dealing with issues like Safari not supporting SameSite=None,
    And the client passes the session as Authorization header:

    Authorization: Session 7wvz4sxcp3chm9quyw015n6ryre29b3u

    Run the standard Django auth & try obtaining user.
    """

    header: str = "Authorization"
    openapi_scheme: str = "session"

    def authenticate(self, request: HttpRequest, token: str | None) -> Any | None:
        engine = import_module(settings.SESSION_ENGINE)
        session_store = engine.SessionStore

        request.session = session_store(token)
        user = auth.get_user(request)

        return user, None
