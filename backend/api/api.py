from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from .users.routers import router as users_router

api = NinjaExtraAPI(title="ReadRats API")
api.register_controllers(NinjaJWTDefaultController)

api.add_router("/users/", users_router)