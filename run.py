from dotenv import load_dotenv
import teamwork
import os

class TeamworkpmStats:
    """ Class to produce stats on TeamworkPM projects """

    def __init__(self, url, key):        
        self.teamworkpm_api_url = url
        self.teamworkpm_api_key = key
    

    def settings(self):
        print("teamworpm_api_url = " + self.teamworkpm_api_url)
        print("teamworkpm_api_key = " + self.teamworkpm_api_key)
    

#\TeamworkStats

#run
load_dotenv()
print("Start")
p1 = TeamworkpmStats(os.getenv("TEAMWORKPM_API_URL"), os.getenv("TEAMWORKPM_API_KEY"))
p1.settings()

