from flask import Flask
app = Flask(__name__)

from secure_river.middlewares.auth import auth
import secure_river.network as network_util

app.before_request(network_util.Network.middleware)
app.before_request(auth)
# import all the routes
from secure_river.views import register, routes
