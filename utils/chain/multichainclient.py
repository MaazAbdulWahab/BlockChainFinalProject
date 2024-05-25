from utils.chain.multichain import MultiChainClient
import json
from settings import settings
import pprint

rpcuser = "multichainrpc"
rpcpassword = "D2UbRkoaprz1ex7wXqgUA2YC3GYN9Xq4diKwpHTJzvvG"
rpchost = "127.0.0.1"
rpcport = "6828"
chainname = settings.CHAIN_NAME
mc = MultiChainClient(
    settings.RPC_HOST, settings.RPC_PORT, settings.RPC_USER, settings.RPC_PASSWORD
)


streamEmployees = "EMPLOYEES_STREAM"
streamContractors = "CONTRACTORS_STREAM"
streamContractorsVerification = "CONTRACTORS_VERIFICATION"
streamContracts = "CONTRACTS"
streamBids = "BIDS"
streamDeliverables = "DELIVERABLES"
streamAwards = "AWARDS"


if not mc.liststreams(streamEmployees):
    mc.create("stream", streamEmployees, True)
    mc.subscribe(streamEmployees)

if not mc.liststreams(streamContractors):
    mc.create("stream", streamContractors, True)
    mc.subscribe(streamContractors)

if not mc.liststreams(streamContractorsVerification):
    mc.create("stream", streamContractorsVerification, True)
    mc.subscribe(streamContractorsVerification)

if not mc.liststreams(streamContracts):
    mc.create("stream", streamContracts, True)
    mc.subscribe(streamContracts)

if not mc.liststreams(streamBids):
    mc.create("stream", streamBids, True)
    mc.subscribe(streamBids)

if not mc.liststreams(streamDeliverables):
    mc.create("stream", streamDeliverables, True)
    mc.subscribe(streamDeliverables)
