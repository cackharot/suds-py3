import unittest

import suds
from suds.client import Client

class TestServiceDefinition(unittest.TestCase):
    def setUp(self):
        self.client = Client('http://www.thomas-bayer.com/axis2/services/BLZService?wsdl')

    def test_service_representation(self):
        string_rep = str(self.client)
        ver = suds.__version__
        build = suds.__build__.split()[1]
        expected = """
Suds ( https://github.com/cackharot/suds-py3 )  version: %s IN  build: %s

Service ( BLZService ) tns="http://thomas-bayer.com/blz/"
   Prefixes (1)
      ns0 = "http://thomas-bayer.com/blz/"
   Ports (2):
      (BLZServiceSOAP11port_http)
         Methods (1):
            getBank(xs:string blz, )
         Types (3):
            detailsType
            getBankResponseType
            getBankType
      (BLZServiceSOAP12port_http)
         Methods (1):
            getBank(xs:string blz, )
         Types (3):
            detailsType
            getBankResponseType
            getBankType
--------------------------------------------------------------------------------""" % (ver, build)
        self.assertEqual(string_rep, expected)

if __name__ == '__main__':
    unittest.main()
