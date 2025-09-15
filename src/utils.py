import json


def read_json(data_user: str) -> list:

    with open(data_user, "r", encoding="utf-8") as file:
        return json.load(file)


# if __name__ == "__main__":
#     data = read_json(r"C:\PythonProgramm\PROJECT\Online_store\products.json")
#     print(data)
