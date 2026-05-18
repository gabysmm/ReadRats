from ninja import Router
from ninja_jwt.tokens import RefreshToken

from apps.users.models import User

from .schemas import RegisterInput, RegisterOutput

router = Router()


@router.post("/register", auth=None, response={201: RegisterOutput, 400: dict})
def register(request, data: RegisterInput):
    if User.objects.filter(email=data.email).exists():
        return 400, {"message": "Email já cadastrado!"}
    user = User.objects.create_user(
        username=data.username, email=data.email, password=data.password
    )
    token = RefreshToken.for_user(user)
    return 201, {"access": str(token.access_token), "refresh": str(token)}
