from utils.chain.multichainclient import (
    mc,
    streamEmployees,
    streamDeliverableCompletion,
    streamDeliveryMarkCompletion,
)
import pprint
from passlib.hash import pbkdf2_sha256
import uuid

"""
for i in range(5):
    mc.getnewaddress()
"""
data = {
    "1": {
        "username": "manager@gmail.com",
        "password": pbkdf2_sha256.hash("manager1234"),
        "role": "MANAGER",
        "address": "1BhFcjofTJXn8CWkduXA9vxbZv9ujd8PK7ZANF",
    },
    "2": {
        "username": "employee1@gmail.com",
        "password": pbkdf2_sha256.hash("employee1"),
        "role": "EMPLOYEE",
        "address": "19eS7hQ9NaeiSLJY4cyZmVzYmW6hNdKig6XBJf",
    },
    "3": {
        "username": "employee2@gmail.com",
        "password": pbkdf2_sha256.hash("employee2"),
        "role": "EMPLOYEE",
        "address": "1SkYuxAQM5eEznrHTE2YHie8PFKBm2Pw5zak8b",
    },
    "4": {
        "username": "employee3@gmail.com",
        "password": pbkdf2_sha256.hash("employee3"),
        "role": "EMPLOYEE",
        "address": "15ypeJ4bfbfSkDUkeMRK9XuZK4Qsj8YUddkKbw",
    },
    "5": {
        "username": "employee4@gmail.com",
        "password": pbkdf2_sha256.hash("employee4"),
        "role": "EMPLOYEE",
        "address": "1Mu6PkdAXCPpaeftFkGKyXprp6AkoVJyEuus3c",
    },
    "6": {
        "username": "employee5@gmail.com",
        "password": pbkdf2_sha256.hash("employee5"),
        "role": "EMPLOYEE",
        "address": "167TMEhwZcHMwuCtjbqARrvs145jrrcGVTX5Vd",
    },
}

"""
for i in data:
    mc.publish(streamEmployees, i, {"json": data[i]})
"""

pprint.pp(
    mc.createmultisig(
        2,
        [
            "1BhFcjofTJXn8CWkduXA9vxbZv9ujd8PK7ZANF",
            "19eS7hQ9NaeiSLJY4cyZmVzYmW6hNdKig6XBJf",
        ],
    )
)


# pprint.pp(mc.grant("4AMvwUo7jgGLLexGXR7jmBFD5zPhAkHqhwSspV", "send"))


# pprint.pp(mc.grant("4AMvwUo7jgGLLexGXR7jmBFD5zPhAkHqhwSspV", "receive"))

"""pprint.pp(
    mc.sendassetfrom(
        "1BhFcjofTJXn8CWkduXA9vxbZv9ujd8PK7ZANF",
        "4AMvwUo7jgGLLexGXR7jmBFD5zPhAkHqhwSspV",
        "asset1",
        10,
    )
)"""
# pprint.pp(mc.getaddressbalances("4AMvwUo7jgGLLexGXR7jmBFD5zPhAkHqhwSspV", 0))

# pprint.pp(mc.listunspent(0, 9999999, ["4AMvwUo7jgGLLexGXR7jmBFD5zPhAkHqhwSspV"]))


pprint.pp(
    mc.createrawsendfrom(
        "4AMvwUo7jgGLLexGXR7jmBFD5zPhAkHqhwSspV",
        {"1SkYuxAQM5eEznrHTE2YHie8PFKBm2Pw5zak8b": {"asset1": 5}},
    )
)


# pprint.pp(
#    mc.issue(
#        "1SkYuxAQM5eEznrHTE2YHie8PFKBm2Pw5zak8b",
#        {"name": "NFTREAL", "fungible": False, "open": True},
#        0,
#    )
# )


# pprint.pp(
#    mc.issuetoken("1SkYuxAQM5eEznrHTE2YHie8PFKBm2Pw5zak8b", "NFTREAL", "token4", 2, 0)
# )


# pprint.pp(

#    mc.send(
#        "1SkYuxAQM5eEznrHTE2YHie8PFKBm2Pw5zak8b",
#       {"NFTREAL": {"token": "token1", "qty": 1}},
#   )
# )

# pprint.pp(
#    mc.issue(
#        "1SbL4BvueQrNVnnAoQaJKp466kDe143Q71xD2",
#        {"name": "NFTDELIVERABLECOMPLETION", "fungible": False, "open": True},
#        0,
#    )
# )

# pprint.pp(
#    mc.issuetoken(
#        "1SbL4BvueQrNVnnAoQaJKp466kDe143Q71xD2",
#        "NFTDELIVERABLECOMPLETION",
#        f"token{str(uuid.uuid4())}",
#        6,
#        0,
#    )
# )


# pprint.pp(mc.gettokenbalances("1SbL4BvueQrNVnnAoQaJKp466kDe143Q71xD2"))
pprint.pp(mc.liststreamitems("EMPLOYEES", False, 99999))
