import os.path

from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleService:
  def __init__(self):
    self.SCOPES = ["https://www.googleapis.com/auth/apps.order", "https://www.googleapis.com/auth/spreadsheets"]

    self.creds = None

    self._reseller_service = None
    self._spreadsheets_service = None

    self.customers = None
    self.subscriptions = None
    self.spreadsheets = None

    if os.path.exists("token.json"):
      self.creds = service_account.Credentials.from_service_account_file("token.json", scopes=self.SCOPES)


    self._reseller_service = build("reseller", "v1", credentials=self.creds) 
    self._spreadsheets_service = build("sheets", "v4", credentials=self.creds)

    self.subscriptions = self._reseller_service.subscriptions
    self.customers = self._reseller_service.customers

    self.spreadsheets = self._spreadsheets_service.spreadsheets

if __name__ == "__main__":
  app = GoogleService()
