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
      # TODO: split it
      network = self.lookup_mcc_mnc(data['mccmnc'])
    network_apparent = self.get_isp_info(data.ip)
    return (network, network_apparent)

  def middleware():
    val = request.values
    if (val['network']):
      # What the client said
      g.networks = self.get_network_id(val['network'])
