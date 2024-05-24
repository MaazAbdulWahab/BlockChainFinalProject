from utils.chain.multichainclient import mc, streamEmployees
import pprint
from passlib.hash import pbkdf2_sha256

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
pprint.pp(mc.liststreamitems(streamEmployees))
