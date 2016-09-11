from mobile_codes import mcc_mnc
import requests
from flask import request, g
from models import Network as NetworkModel
from querystring_parser import parser
from app import db

class Network(object):

    def lookup_mcc_mnc(mcc, mnc):
        return mcc_mnc(mcc, mnc)

    def get_isp_info(ip):
        url = "http://ip-api.com/json/" + ip
        return requests.get(url).json()

    def get_network_id(data):
        if (data['type'] == 'mobile'):
            network = NetworkModel.objects(db.Q(mobile=True) & db.Q(mccmnc=data['mccmnc'])).only('region', 'isp', 'mccmnc')
            print(network.to_json())
            # network_apparent = Network.get_isp_info(data['ip'])
        return (network, None)

    @staticmethod
    def middleware():
        g.networks = None
        data = request.values
        if ('network' in data):# and data['network'] == '1'):
            g.networks = Network.get_network_id(data)
        return None

    # @staticmethod
    # def get_isp_code(name):
