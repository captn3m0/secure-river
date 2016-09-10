from mobile_codes import mcc_mnc
import requests

class Network(object):

  def lookup_mcc_mnc(mcc, mnc):
    return mcc_mnc(mcc, mnc)

  def get_isp_info(ip):
    url = "http://ip-api.com/json/" + ip
    return requests.get(url).json()
