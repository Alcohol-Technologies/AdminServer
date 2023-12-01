import json
def readUsers(file_name):
    with open(file_name, encoding="utf8") as file:
        users_data = json.load(file)

    if users_data["status"] != "ok":
        return "error"

    users_list = users_data["users"]

    return users_list

