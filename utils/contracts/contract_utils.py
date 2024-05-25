from utils.chain.multichainclient import (
    mc,
    streamContracts,
    streamBids,
    streamDeliverables,
    streamAwards,
    streamDeliverableCompletion,
    streamDeliveryMarkCompletion,
    streamAwardsVerify,
)
from typings import (
    Contract,
    Bid,
    Deliverable,
    DeliverableCompletion,
    MarkDeliverableCompletion,
    ContractAward,
    VerifyAward,
)
from typing import List
import json


def post_contracts(contract: Contract, address: str):
    contract = contract.model_dump()
    id = contract["id"]
    del contract["id"]
    mc.publishfrom(address, streamContracts, id, {"json": contract})


def get_awards():
    awards = mc.liststreamitems(streamAwards)
    awards_verified = mc.liststreamitems(streamAwardsVerify)
    awards_list = []
    for aw in awards:

        aw_data = aw["data"]["json"]
        aw_data = json.loads(json.dumps(aw_data))
        aw_id = aw["keys"][0]
        aw_data.update({"id": aw_id})

        for awv in awards_verified:
            awv_data = awv["data"]["json"]
            awv_data = json.loads(json.dumps(awv_data))
            awv_id = awv["keys"][0]
            awv_data.update({"id": awv_id})
            if aw_data["id"] == awv_data["award_id"]:
                aw_data.update({"award_verified": awv_data})
                break

        awards_list.append(aw_data)

    return awards_list


def get_contracts():

    contracts_list = []
    contracts = mc.liststreamitems(streamContracts)
    awards = get_awards()
    for con in contracts:

        con_data = con["data"]["json"]
        contract = json.loads(json.dumps(con_data))
        contract_id = con["keys"][0]
        contract.update({"id": contract_id})
        awards_of_this = []
        for aw in awards:
            if aw["contract_id"] == contract_id:
                awards_of_this.append(aw)
        if len(awards_of_this) > 0:
            contract.update({"awards": awards_of_this})
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


def award_contract_(award: ContractAward, address: str):
    award = award.model_dump()
    id = award["id"]
    del award["id"]
    mc.publishfrom(address, streamAwards, id, {"json": award})


def verify_award_(award: VerifyAward, address: str):
    award = award.model_dump()
    id = award["id"]
    del award["id"]
    mc.publishfrom(address, streamAwardsVerify, id, {"json": award})


def create_deliverables_(deliverables: List[Deliverable], address: str):
    for d in deliverables:
        deli = d.model_dump()
        id = deli["id"]
        del deli["id"]
        mc.publishfrom(address, streamDeliverables, id, {"json": deli})


def get_deliverables(contract_id):
    award = None
    awards = mc.liststreamitems(streamDeliverables)

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
    deliverables_marked_completed = mc.liststreamitems(streamDeliveryMarkCompletion)

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

                    for dmc in deliverables_marked_completed:
                        dmc_data = dmc["data"]["json"]
                        dmc_data = json.loads(json.dumps(dmc_data))
                        dmc_id = dmc["keys"][0]
                        dmc_data.update({"id": dmc_id})
                        if ddc_data["id"] == dmc_data["completed_deliverable_id"]:
                            ddc_data.update({"delivery_completed_marked": dmc_data})
                            break

                    deliverable_data.update({"deliverable_completion": {ddc_data}})
                    break

            deliverable_list.append(deliverable_data)

    return deliverable_list


def submit_deliverable_completion(com: DeliverableCompletion, address: str):
    com = com.model_dump()
    id = com["id"]
    del com["id"]
    mc.publishfrom(address, streamDeliverableCompletion, id, {"json": com})


def get_completed_deliverables():
    deliverables_completion = mc.liststreamitems(streamDeliverableCompletion)
    deliverables_marked_completed = mc.liststreamitems(streamDeliveryMarkCompletion)
    deliverables_completion_list = []
    for ddc in deliverables_completion:

        ddc_data = ddc["data"]["json"]
        ddc_data = json.loads(json.dumps(ddc_data))
        ddc_id = ddc["keys"][0]
        ddc_data.update({"id": ddc_id})

        for dmc in deliverables_marked_completed:
            dmc_data = dmc["data"]["json"]
            dmc_data = json.loads(json.dumps(dmc_data))
            dmc_id = dmc["keys"][0]
            dmc_data.update({"id": dmc_id})
            if ddc_data["id"] == dmc_data["completed_deliverable_id"]:
                ddc_data.update({"delivery_completed_marked": dmc_data})
                break

        deliverables_completion_list.append(ddc_data)

    return deliverables_completion_list


def mark_deliverable_as_complete(comp: MarkDeliverableCompletion, address: str):
    comp = comp.model_dump()
    id = comp["id"]
    del comp["id"]
    mc.publishfrom(address, streamDeliveryMarkCompletion, id, {"json": comp})
