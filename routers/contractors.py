from fastapi import APIRouter, Depends
from typings import Bid, DeliverableCompletion
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer
from utils.contracts.contract_utils import (
    get_contracts,
    place_bid_,
    get_deliverables,
    submit_deliverable_completion,
)
from utils.auth.dependencies import require_role
import uuid

contractors_router = APIRouter(
    prefix="/contractors",
    tags=["contractors"],
)


@contractors_router.get("/view-open-contracts")
async def view_open_contracts(user=Depends(require_role("CONTRACTOR"))):
    return get_contracts(only_active=True)


@contractors_router.post("/place-bid/{contract_id}")
async def place_bid(
    bid: Bid, contract_id: str, user=Depends(require_role("CONTRACTOR"))
):
    bid.id = str(uuid.uuid4())
    bid.contract_id = contract_id
    bid.contractor_id = user["id"]
    place_bid_(bid, user["address"])
    return bid


@contractors_router.post("/mark-deliverable-complete")
async def mark_deliverable_complete(
    dc: DeliverableCompletion, user=Depends(require_role("CONTRACTOR"))
):
    dc.id = str(uuid.uuid4())
    submit_deliverable_completion(dc, user["address"])
    return dc


@contractors_router.get("/get-contracts-awarded")
def get_awarded_contracts(user=Depends(require_role("CONTRACTOR"))):
    return get_contracts()


@contractors_router.get("/view-deliverables/{contract_id}")
async def get_deliverables_(
    contract_id: str = None, user=Depends(require_role("CONTRACTOR"))
):
    return get_deliverables(contract_id)


@contractors_router.get("/view-awards")
async def get_awards(active: bool = True):
    pass
