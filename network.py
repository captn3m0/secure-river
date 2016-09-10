from mobile_codes import mcc_mnc
import requests
from flask import request, g

class Network(object):

    def lookup_mcc_mnc(mcc, mnc):
        return mcc_mnc(mcc, mnc)

    def get_isp_info(ip):
        url = "http://ip-api.com/json/" + ip
        return requests.get(url).json()

    def get_network_id(data):
        if (data['type'] == 'mobile'):
            mcc,mnc = (data['mccmnc'][0:3], data['mccmnc'][3:])
            network = Network.lookup_mcc_mnc(mcc, mnc)
            network_apparent = Network.get_isp_info(data['ip'])
        return (network, network_apparent)

    @staticmethod
    def middleware():
        val = request.values
        if ('network' in val):
            g.networks = self.get_network_id(val['network'])
        return None

    # @staticmethod
    # def get_isp_code(name):
