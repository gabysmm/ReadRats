from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from .users.routers import router as users_router

api = NinjaExtraAPI(title="ReadRats API", auth=JWTAuth())
api.register_controllers(NinjaJWTDefaultController)

api.add_router("/users/", users_router)