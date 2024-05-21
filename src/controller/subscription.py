from flask import Blueprint

from service.subscription import SubscriptionService

subscriptionsService = SubscriptionService()

subscriptions = Blueprint('subscriptions', __name__, url_prefix='/subscriptions')

@subscriptions.route('/get/<customerId>')
def get_subscriptions_from_customer(customerId):
  return subscriptionsService.get_subscriptions_from_customer(customerId)
