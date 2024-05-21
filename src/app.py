
from flask import Flask
from controller.subscription import subscriptions
class App:
  def __init__(self):
    self.app = Flask(__name__)
    self._register_blueprints()    

  def _register_blueprints(self):
    self.app.register_blueprint(subscriptions)

  def run(self):
    self.app.run()

app = App()
app.run()
