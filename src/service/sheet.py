from service.google import GoogleService

class SheetService(GoogleService):
  def __init__(self):
    super().__init__()
    self.spreadsheets = GoogleService().spreadsheets
    self.SAMPLE_SPREADSHEET_ID = "1oo9GSybxW2wxcgFVSxX_dEF5Vm6dD-Y6xCbizeDAT7c"
    self.SAMPLE_RANGE_NAME = "relatorios!A:B"

  def get_tables(self):
    result = (
        self.spreadsheets().values()
        .get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, range=self.SAMPLE_RANGE_NAME)
        .execute()
    )

    return result.get("values", [])
  
  def append_table(self, values):
    body = {"values": [values]}
    result = (
        self.spreadsheets()
        .values()
        .append(
            spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
            range=self.SAMPLE_RANGE_NAME,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )
    return result

