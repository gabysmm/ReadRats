from ninja import Router
from apps.community.models import Community, Membership
from .schemas import CreateCommunityInput, CreateCommunityOutput

router = Router()

@router.post("/", response={201: CreateCommunityOutput, 401: dict})
def create_community(request, data: CreateCommunityInput):
    if not request.user.is_authenticated:
        return 401, {"message": "não autenticado"}
    community = Community.objects.create(
        name = data.name,
        description = data.description,
        type_community = data.type_community,
        creator = request.user,
    )
    membership = Membership.objects.create(
        user = request.user,
        community = community,
        role = 'admin',
    )
    return 201, community