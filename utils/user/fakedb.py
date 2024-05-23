from copy import deepcopy

db = {
    "1": {
        "username": "maazabdulwahab@outlook.com",
        "password": "test1234",
        "role": "admin",
    },
    "2": {
        "username": "maazwahab19@gmail.com",
        "password": "test5678",
        "role": "contractor",
    },
}


def getuser(id: str):
    return db.get(id)


def finduser(username: str, password: str):
    foundUser = None
    for ids in db:
        if db[ids]["username"] == username:
            foundUser = deepcopy(db[ids])
            if foundUser["password"] == password:
                foundUser.update({"id": ids})
                return foundUser
            else:
                return None
    return None
