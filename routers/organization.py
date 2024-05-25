from fastapi import APIRouter
from typings import (
    Contract,
    ContractAward,
    Deliverable,
    MarkDeliverableCompletion,
    VerifyAward,
)
from typing import List, Union
from datetime import datetime
from uuid import uuid4
from utils.user.user_utils import all_contractors, update_contractor
from utils.auth.dependencies import require_role
from fastapi import Depends
from utils.chain.multichainclient import mc
from utils.contracts.contract_utils import (
    post_contracts,
    get_contracts,
    get_bids,
    create_deliverables_,
    get_deliverables,
    get_completed_deliverables,
    mark_deliverable_as_complete,
    award_contract_,
)
import uuid

organization_router = APIRouter(
    prefix="/organization",
    tags=["organization"],
)


@organization_router.get("/get-contractors")
async def get_contractors(
    id: str = None, user=Depends(require_role(["EMPLOYEE", "MANAGER"]))
):
    print("user is")
    print(user)
    return all_contractors(id)


@organization_router.put("/verify-contractor/{contractor_id}")
async def verify_contractor(
    contractor_id: str, user=Depends(require_role(["EMPLOYEE", "MANAGER"]))
):
    contractor = all_contractors(contractor_id)
    signature = mc.signmessage(user["address"], "VERIFIED")
    verification_data = {
        "verified": True,
        "verified_by_id": user["id"],
        "verified_by_address": user["address"],
        "signature": signature,
    }

    update_contractor(contractor_id, verification_data)
    return contractor


@organization_router.post("/post-contract")
async def post_contract(contract: Contract, user=Depends(require_role("EMPLOYEE"))):
    contract.id = str(uuid.uuid4())
    post_contracts(contract, user["address"])
    return contract


@organization_router.get("/view-contracts")
async def view_contracts(
    contract_id: str = None,
    active: bool = False,
    awarded: bool = False,
    contractor_id: str = None,
    complete_till__gte: datetime = None,
    complete_till__lte: datetime = None,
):

    return get_contracts()


@organization_router.get("/view-bids/{contract_id}")
async def view_bids(
    contract_id: str, user=Depends(require_role(["EMPLOYEE", "MANAGER"]))
):
    return get_bids(contract_id)


@organization_router.post("/award-contract")
async def award_contract(
    contract_award: ContractAward,
    user=Depends(require_role("EMPLOYEE")),
):
    signature = mc.signmessage(user["address"], "AWARDED")
    contract_award.id = str(uuid.uuid4())
    contract_award.signature = signature
    contract_award.awarded_by_address = user["addres"]
    contract_award.awarded_by = user["id"]
    award_contract_(contract_award, user["address"])
    return contract_award


@organization_router.post("/verify-award")
async def verify_award(
    contract_award: VerifyAward,
    user=Depends(require_role("MANAGER")),
):
    signature = mc.signmessage(user["address"], "AWARDED")
    contract_award.id = str(uuid.uuid4())
    contract_award.signature = signature
    contract_award.verified_by_address = user["addres"]
    contract_award.verified_by = user["id"]
    award_contract_(contract_award, user["address"])
    return contract_award


@organization_router.post("/create-deliverables/")
async def create_deliverables(
    deliverables: List[Deliverable],
    user=Depends(require_role("EMPLOYEE")),
):
    for d in deliverables:
        d.id = str(uuid.uuid4())
        d.created_by = user["id"]
        d.created_by_address = user["address"]
    create_deliverables_(deliverables, user["address"])
    return deliverables


@organization_router.post("/view-deliverables/{contract_id}")
async def view_deliverables(
    contract_id: str, user=Depends(require_role(["EMPLOYEE", "MANAGER"]))
):
    return get_deliverables(contract_id)


@organization_router.get("/view-completed-deliverables")
async def get_completed_deliverables_(
    user=Depends(require_role(["EMPLOYEE", "MANAGER"]))
):
    return get_completed_deliverables()


@organization_router.post("mark-deliverable-complete")
async def mark_deliverable_complete(
    mark: MarkDeliverableCompletion,
    user=Depends(require_role("EMPLOYEE")),
):
    signature = mc.signmessage(user["address"], "COMPLETED")
    mark.id = str(uuid.uuid4())
    mark.signature = signature
    mark.marked_by_address = user["addres"]
    mark.marked_by = user["id"]
    mark_deliverable_as_complete(mark, user["address"])
    return mark
