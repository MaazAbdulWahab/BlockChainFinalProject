from fastapi import APIRouter
from typings import Contract, ContractAward, Deliverable, MarkDeliverableCompletion
from typing import List
from datetime import datetime
from uuid import uuid4

organization_router = APIRouter(
    prefix="/organization",
    tags=["organization"],
)


@organization_router.post("/post-contract")
async def post_contract(contract: Contract):
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

    return {"contracts": []}


@organization_router.get("/view-bids/{contract_id}")
async def view_bids(contract_id: str):
    return


@organization_router.post("/award-contract")
async def award_contract(contract_award: ContractAward):
    return contract_award


@organization_router.post("/create-deliverables/{contract_id}")
async def create_deliverables(deliverables: List[Deliverable]):
    return deliverables


@organization_router.post("/view-deliverables/{contract_id}")
async def view_deliverables(contract_id: str):
    pass


@organization_router.post("mark-deliverable-complete")
async def mark_deliverable_complete(mark: MarkDeliverableCompletion):
    pass
