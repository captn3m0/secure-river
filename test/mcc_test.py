import unittest

from network.mcc import MCC

class mcc_test(unittest.TestCase):
  def runTest(self):
    details = MCC.get_mcc_details(405,862)
    assert details['network'] == 'LOOP'
    assert details['operator'] == 'LOOP'
    assert details['mnc'] == '862'
    assert details['mcc'] == '405'
    assert details['region'] == 'Karnataka'

if __name__ == '__main__':
    unittest.main()
