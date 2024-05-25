from utils.chain.multichainclient import (
    mc,
    streamContracts,
    streamBids,
    streamDeliverables,
    streamAwards,
    streamDeliverableCompletion,
)
from typings import Contract, Bid, Deliverable, DeliverableCompletion
from typing import List
import json


def post_contracts(contract: Contract, address: str):
    contract = contract.model_dump()
    id = contract["id"]
    del contract["id"]
    mc.publishfrom(address, streamContracts, id, {"json": contract})


def get_contracts():

    contracts_list = []
    contracts = mc.liststreamitems(streamContracts)

    for con in contracts:

        con_data = con["data"]["json"]
        contract = json.loads(json.dumps(con_data))
        contract_id = con["keys"][0]
        contract.update({"id": contract_id})
        contracts_list.append(contract)

    return contracts_list


def place_bid_(bid: Bid, address: str):
    contract = contract.model_dump()
    id = contract["id"]
    del contract["id"]
    mc.publishfrom(address, streamBids, id, {"json": contract})


def get_bids(contract_id):
    bids_list = []
    bids = mc.liststreamitems(streamBids)

    for bd in bids:

        bid_data = bd["data"]["json"]
        bid_data = json.loads(json.dumps(bid_data))
        bid_id = bd["keys"][0]
        bid_data.update({"id": bid_id})
        if bid_data["contract_id"] == contract_id:
            bids_list.append(bid_data)

    return bid_data


def create_deliverables_(deliverables: List[Deliverable], address: str):
    for d in deliverables:
        deli = d.model_dump()
        id = deli["id"]
        del deli["id"]
        mc.publishfrom(address, streamDeliverables, id, {"json": deli})


def get_deliverables(contract_id):
    award = None
    awards = mc.liststreamitems(streamAwards)

    for aw in awards:

        award_data = aw["data"]["json"]
        award_data = json.loads(json.dumps(award_data))
        award_id = aw["keys"][0]
        award_data.update({"id": award_id})
        if award_data["contract_id"] == contract_id:
            award = award_data
    deliverable_list = []
    deliverables = mc.liststreamitems(streamDeliverables)
    deliverables_completion = mc.liststreamitems(streamDeliverableCompletion)
    for dw in deliverables:

        deliverable_data = dw["data"]["json"]
        deliverable_data = json.loads(json.dumps(deliverable_data))
        deliverable_id = dw["keys"][0]
        deliverable_data.update({"id": deliverable_id})
        if deliverable_data["award_id"] == award["id"]:

            for ddc in deliverables_completion:

                ddc_data = ddc["data"]["json"]
                ddc_data = json.loads(json.dumps(ddc_data))
                ddc_id = ddc["keys"][0]
                ddc_data.update({"id": ddc_id})
                if deliverable_data["deliverable_id"] == deliverable_data["id"]:
                    deliverable_data.update(
                        {
                            "deliverable_completion": {
                                "deliverable_complete": ddc_data[
                                    "deliverable_complete"
                                ],
                                "remarks": ddc_data["remarks"],
                                "cost": ddc_data["cost"],
                                "documents": ddc_data["documents"],
                                "completed": ddc_data["completed"],
                            }
                        }
                    )
                    break

            deliverable_list.append(deliverable_data)

    return deliverable_list


def submit_deliverable_completion(com: DeliverableCompletion, address: str):
    comp = com.model_dump()
    id = com["id"]
    del com["id"]
    mc.publishfrom(address, streamDeliverableCompletion, id, {"json": com})


def get_completed_deliverables():
    deliverables_completion = mc.liststreamitems(streamDeliverableCompletion)
    deliverables_completion_list = []
    for ddc in deliverables_completion:

        ddc_data = ddc["data"]["json"]
        ddc_data = json.loads(json.dumps(ddc_data))
        ddc_id = ddc["keys"][0]
        ddc_data.update({"id": ddc_id})
        deliverables_completion_list.append(ddc_data)
    return deliverables_completion_list