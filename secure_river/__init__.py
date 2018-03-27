from flask import Flask
app = Flask(__name__)

from secure_river.middlewares.auth import auth
from secure_river.network import Network

app.before_request(Network.middleware)
app.before_request(auth)
# import all the routes
from secure_river.views import register, routes, network, job
