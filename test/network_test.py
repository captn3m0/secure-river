import unittest
from network import Network

class NetworkTest(unittest.TestCase):
  def test_mcc_code(self):
    details = Network.lookup_mcc_mnc('405','861')
    assert details[0] == '405'
    assert details[1] == '861'
    assert details[2] == 'Jio'
    assert details[3] == 'Karnataka'

  def test_hello(self):
    details = Network.get_isp_info('182.74.201.254')
    assert details['org'] == 'Bharti Airtel'
    assert details['isp'] == 'Bharti Broadband'
    assert details['city'] == 'New Delhi (Okhla Phase III)'
    assert details['regionName'] == 'NCT'
