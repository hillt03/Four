import json
import requests

def get_json(filepath):
    """
    Returns a dict from a json file.
    """
    with open(filepath, "r") as f:
        return json.load(f)

def get_json_from_api(json_url, params=None):
    req = requests.get(json_url, params=params) if params else requests.get(json_url)
    return req.json() if req.ok else None

def get_html(url):
    req = requests.get(url)
    return req.text() if req.ok else None