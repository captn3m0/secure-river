import requests

from flask import request, g

from mobile_codes import mcc_mnc
from secure_river.models import Network as NetworkModel
from querystring_parser import parser

class Network(object):

    def lookup_mcc_mnc(mcc, mnc):
        return mcc_mnc(mcc, mnc)

    def get_isp_info(ip):
        url = "http://ip-api.com/json/" + ip
        return requests.get(url).json()

    def get_network_id(data):
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)

        if (data['type'] == 'mobile'):
            network = NetworkModel.find_by_mcc_mnc(data['mccmnc'])
        isp_info = Network.get_isp_info(ip)
        network_apparent = NetworkModel.find_or_create(isp_info)

        if (data['type'] == 'mobile'):
            if ((network.isp == network_apparent.isp) and (network.region == network_apparent.region)):
                network_apparent = network
        else:
            network = network_apparent

        return (network, network_apparent)

    @staticmethod
    def middleware():
        g.networks = None
        data = request.values
        if ('network' in data):# and data['network'] == '1'):
            g.networks = Network.get_network_id(data)
        return None

    # @staticmethod
    # def get_isp_code(name):
