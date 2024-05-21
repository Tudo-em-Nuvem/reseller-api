from service.reseller import Reseller

class SubscriptionService(Reseller):
  def __init__(self):
    super().__init__()
    self.subscriptions = Reseller().subscriptions

  def get_subscriptions_from_customer(self, customerId):
    results = self.subscriptions().list(customerId=customerId).execute()
    return results.get("subscriptions", [])

  def suspend_all_subscription_from_customer(self, customerId) -> None:
    subscriptions = self.get_subscriptions_from_customer(customerId)
    for subscription in subscriptions:
      if subscription["billingMethod"] == "OFFLINE": continue
      try:
        self.suspend_subscription(subscription["customerId"], subscription["subscriptionId"])
      except Exception as e:
        raise Exception("Error: {0}".format(e))

  def activate_all_subscription_from_customer(self, customerId) -> None:
    subscriptions = self.get_subscriptions_from_customer(customerId)
    for subscription in subscriptions:

      if subscription["status"] == "ACTIVE": continue

      try:
        self.activate_subscription(customerId, subscription["subscriptionId"])
      except Exception as e:
        print("Error: {0}".format(e))
  
  def activate_subscription(self, customerId, subscriptionId):
    self.subscriptions().activate(customerId=customerId, subscriptionId=subscriptionId).execute()

  def suspend_subscription(self, customerId, subscriptionId):
    self.subscriptions().suspend(customerId=customerId, subscriptionId=subscriptionId).execute()
