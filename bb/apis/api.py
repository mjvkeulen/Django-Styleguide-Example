from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from bb.authentication.api import router as authentication_router
from bb.users.api import router as users_router

api = NinjaExtraAPI(csrf=False)

# TODO Stack: Use router approach so we can drop the dependency on ninja extra
# https://eadwincode.github.io/django-ninja-jwt/customizing_token_claims/#use-django-ninja-router
api.register_controllers(NinjaJWTDefaultController)

api.add_router("/users/", users_router)
api.add_router("/authentication/", authentication_router)
