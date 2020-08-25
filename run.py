from dotenv import load_dotenv
import os
import requests
import json
import sys, subprocess

import urllib.parse as urlparse
from urllib.parse import parse_qs


class TeamworkpmStats:
    """ Class to produce stats on TeamworkPM projects """

    def __init__(self, clientId, clientSecret, redirectUri):        
        self.CLIENT_ID = clientId
        self.CLIENT_SECRET = clientSecret
        self.REDIRECT_URI = redirectUri

    def settings(self):
        print("CLIENT_ID = " + self.CLIENT_ID)
        print("CLIENT_SECRET = " + self.CLIENT_SECRET)
        print("REDIRECT_URI = " + self.REDIRECT_URI)
       

    def openUrl(self,url):
        if sys.platform=='win32':
            os.startfile(url)
        elif sys.platform=='darwin':
            subprocess.Popen(['open', url])
        else:
            try:
                subprocess.Popen(['xdg-open', url])
            except OSError:
                print('Please open a browser on: '+url)


    def getCodeFromUser(self):
        redirectResponse = input("Enter response url:")
        parsed = urlparse.urlparse(redirectResponse)
        return parse_qs(parsed.query)['code']


    def updateAccessToken(self):
        """
        Reference 
        https://developer.teamwork.com/projects/authentication-questions/app-login-flow
        """

        url = "https://www.teamwork.com/launchpad/login?redirect_uri="+self.REDIRECT_URI+"&client_id="+self.CLIENT_ID+""
        self.openUrl(url)

        code = self.getCodeFromUser()


        body_params = {"code": code,
                        "client_secret": self.CLIENT_SECRET,
                        "redirect_uri": self.REDIRECT_URI,
                        "client_id": self.CLIENT_ID}

        url='https://www.teamwork.com/launchpad/v1/token.json'
        response = requests.post(url, data=body_params) 

        if(response.status_code==200):
            self.parseResponse(response.text)
            return True

        else:
            print("Error with response")
            exit()


    def parseResponse(self,jsonResponse):
        token_raw = json.loads(jsonResponse)
  
        self.accessToken = token_raw["access_token"]

        self.installation_id = token_raw["installation"]["id"]
        self.installation_name = token_raw["installation"]["name"]
        self.installation_url = token_raw["installation"]["url"]
        self.installation_region = token_raw["installation"]["region"]
        self.installation_logo = token_raw["installation"]["logo"]
        self.installation_loginstarttext = token_raw["installation"]["loginStartText"]
        self.installation_apiendpoint = token_raw["installation"]["apiEndPoint"]

        self.installation_projectsenabled = token_raw["installation"]["projectsEnabled"]
        self.installation_deskenabled = token_raw["installation"]["deskEnabled"]
        self.installation_chatenabled = token_raw["installation"]["chatEnabled"]        

        self.installation_company_id = token_raw["installation"]["company"]["id"]
        self.installation_company_name = token_raw["installation"]["company"]["name"]
        self.installation_company_logo = token_raw["installation"]["company"]["logo"]       

        self.user_id = token_raw["user"]["id"]       
        self.user_firstname = token_raw["user"]["firstName"]      
        self.user_lastname = token_raw["user"]["lastName"]  
        self.user_email = token_raw["user"]["email"] 



    def getAccount(self):
        url=self.installation_url+"account.json"      
        print(url)  
        headers = {"Authorization": "Bearer {}".format(self.accessToken)}
        response = requests.get(url=url,headers=headers)

        print(response)
        if(response.status_code==200):
            print(response.text)

        else:
            print("Error with response on getAccount()")
            exit()



    def run(self):
        print("Run")
        self.updateAccessToken()
        self.getAccount()



#\TeamworkStats

#run
load_dotenv()
print("Start")
p1 = TeamworkpmStats(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), os.getenv("REDIRECT_URI"))
p1.run()

