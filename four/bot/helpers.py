import json

def get_json(filepath):
    """
    Returns a dict from a json file.
    """
    with open(filepath, "r") as f:
        return json.load(f)
