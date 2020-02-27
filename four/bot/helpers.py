import json

def get_json(filepath):
    """
    Returns a dict from a json file.
    """
    with open(filepath, "r") as f:
        return json.load(f)

def get_secrets(filepath):
    """
    Returns (discord token: str, pandascore token: str)
    """
    data = get_json(filepath)
    return data["DISCORD_TOKEN"], data["PANDASCORE_TOKEN"]