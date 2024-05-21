from flask import Blueprint

from service.subscription import SubscriptionService

subscriptionsService = SubscriptionService()

subscriptions = Blueprint('subscriptions', __name__, url_prefix='/subscriptions')

@subscriptions.route('/<customerId>')
def get_subscriptions_from_customer(customerId):
  return subscriptionsService.get_subscriptions_from_customer(customerId), 200

@subscriptions.route('/suspend/<customerId>')
def suspend_all_subscription_from_customer(customerId):
  subscriptionsService.suspend_all_subscription_from_customer(customerId)
  return 200

@subscriptions.route('/activate/<customerId>')
def activate_all_subscription_from_customer(customerId):
  subscriptionsService.activate_all_subscription_from_customer(customerId)
  return 200
