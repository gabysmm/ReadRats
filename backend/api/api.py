from ninja import NinjaAPI
from .users.routers import router as users_router

api = NinjaAPI()
api.add_router("/users/", users_router)