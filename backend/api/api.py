from ninja import NinjaAPI
from .users.routers import router as users_router

api = NinjaAPI(title="ReadRats API")
api.add_router("/users/", users_router)