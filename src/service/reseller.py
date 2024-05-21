import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class Reseller:
  def __init__(self):
    self.SCOPES = ["https://www.googleapis.com/auth/apps.order"]

    self.creds = None
    self._service = None
    self.subscriptions = None
    self.spreadsheets = None

    if os.path.exists("token.json"):
      self.creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)

    if not self.creds or not self.creds.valid:
  
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
  
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", self.SCOPES
        )

        self.creds = flow.run_local_server(port=0)

      with open("token.json", "w") as token:
        token.write(self.creds.to_json())

    self._service = build("reseller", "v1", credentials=self.creds)
    self.subscriptions = self._service.subscriptions
    self.spreadsheets = self._service.spreadsheets

if __name__ == "__main__":
  app = Reseller()
