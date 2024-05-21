from service.resseler import Reseller

class CustomerService(Reseller):
  def __init__(self):
    super().__init__()
    self.service = Reseller()._service

  def get_customer(self, customerId):
    results = self.service.customers().get(customerId=customerId).execute()
    return results
