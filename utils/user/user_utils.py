from utils.chain.multichainclient import mc, streamEmployees, streamContractors
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
            break

    if user and pbkdf2_sha256.verify(password, user.get("password")):
        return user
    else:
        return None
