from utils.chain.multichainclient import (
    mc,
    streamEmployees,
    streamContractors,
    streamContractorsVerification,
)
import json
from passlib.hash import pbkdf2_sha256


def finduser(username: str, password: str):
    user = None
    employees = mc.liststreamitems(streamEmployees)

    for emp in employees:
        emp_data = emp["data"]["json"]
        if emp_data.get("username") == username:
            user = json.loads(json.dumps(emp_data))
            user.update({"id": emp["keys"][0]})
            break

    contractors = mc.liststreamitems(streamContractors)

    for con in contractors:
        con_data = con["data"]["json"]
        if con_data.get("username") == username:
            user = json.loads(json.dumps(con_data))
            user.update({"id": con["keys"][0]})
            userverification = mc.liststreamkeyitems(
                streamContractorsVerification, con["keys"][0]
            )
            if userverification:
                user.update(json.loads(json.dumps(userverification[0]["data"]["json"])))
            break

    if user and pbkdf2_sha256.verify(password, user.get("password")):
        return user
    else:
        return None


def getuser(id: str):
    user = None
    employees = mc.liststreamitems(streamEmployees)

    for emp in employees:

        if emp["keys"][0] == id:
            emp_data = emp["data"]["json"]
            user = json.loads(json.dumps(emp_data))
            user.update({"id": emp["keys"][0]})
            break

    contractors = mc.liststreamitems(streamContractors)

    for con in contractors:
        if con["keys"][0] == id:
            con_data = con["data"]["json"]
            user = json.loads(json.dumps(con_data))
            user.update({"id": con["keys"][0]})
            userverification = mc.liststreamkeyitems(
                streamContractorsVerification, con["keys"][0]
            )
            if userverification:
                user.update(json.loads(json.dumps(userverification[0]["data"]["json"])))

            break

    return user


def create_contractor(id: str, contractor):
    newAddress = mc.getnewaddress()
    contractor.update({"address": newAddress})
    mc.publish(streamContractors, id, {"json": contractor})
    return contractor


def update_contractor(id: str, contractor):

    mc.publish(streamContractorsVerification, id, {"json": contractor})
    return contractor


def all_contractors(id: str = None):
    contractors = mc.liststreamitems(streamContractors)
    contractors_list = []
    for con in contractors:

        con_data = con["data"]["json"]
        user = json.loads(json.dumps(con_data))
        user_id = con["keys"][0]
        user.update({"id": user_id})
        userverification = mc.liststreamkeyitems(streamContractorsVerification, user_id)
        if userverification:
            user.update(json.loads(json.dumps(userverification[0]["data"]["json"])))

        if id and id == user_id:
            return user
        contractors_list.append(user)
    return contractors_list
