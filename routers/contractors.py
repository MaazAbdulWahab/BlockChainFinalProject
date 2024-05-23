from fastapi import APIRouter
from typings import Bid, DeliverableCompletion
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer

contractors_router = APIRouter(
    prefix="/contractors",
    tags=["contractors"],
)


@contractors_router.get("/view-open-contracts")
async def view_open_contracts():
    return


@contractors_router.post("/place-bid")
async def place_bid(bid: Bid):
    return bid


@contractors_router.post("/mark-deliverable-complete")
async def mark_deliverable_complete(dc: DeliverableCompletion):
    return dc


@contractors_router.get("/view-deliverables")
async def get_deliverables(active: bool = True, contract_id: str = None):
    pass


@contractors_router.get("/view-awards")
async def get_awards(active: bool = True):
    pass
