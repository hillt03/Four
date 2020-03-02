import requests
from datetime import datetime, timedelta

class PandaScoreWrapper():
    """
    Wrapper for the PandaScore API.
    """
    def __init__(self, api_token):
        self.api_token = api_token
        
    
    def get_formatted_time(self, input_time):
        if not input_time:
            return "No start time supplied."
        time = (datetime.fromisoformat(input_time[:-1]) + timedelta(hours=7)).strftime("%m/%d %I:%M %p")
        return str(time)
        


    def get_upcoming_matches(self, amount_of_matches=25):
        params = {"token": self.api_token, "per_page": amount_of_matches}
        matches = requests.get("https://api.pandascore.co/csgo/matches/upcoming", params=params)
        if matches.status_code != 200:
            return None
        return matches.json()




def main():
    pass

if __name__ == "__main__":
    main()