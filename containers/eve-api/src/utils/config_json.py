import json

def read_json(filepath: str):
    try:
        with open(filepath) as file:
            data: dict = json.loads(file.read())
            return data
    except Exception as e:
        raise e