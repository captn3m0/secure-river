import unittest
from secure_river.veritaserum import Veritaserum

class VeritaserumTest(unittest.TestCase):
    def test_process(self):
        v = Veritaserum('https://hs.tatadocomo.com')
        res = v.process()
        assert res['ip'] != None
        assert res['tcp'] == False
        assert res['http'] == None
        assert res['https'] != None

