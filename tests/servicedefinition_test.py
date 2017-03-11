import unittest

import suds
from suds.client import Client

class TestServiceDefinition(unittest.TestCase):
    def setUp(self):
        self.client = Client('http://www.webservicex.com/globalweather.asmx?WSDL')

    def test_service_representation(self):
        string_rep = str(self.client)
        ver = suds.__version__
        build = suds.__build__.split()[1]
        expected = """
Suds ( https://github.com/cackharot/suds-py3 )  version: %s IN  build: %s

Service ( GlobalWeather ) tns="http://www.webserviceX.NET"
   Prefixes (0)
   Ports (2):
      (GlobalWeatherSoap)
         Methods (2):
            GetCitiesByCountry(xs:string CountryName, )
            GetWeather(xs:string CityName, xs:string CountryName, )
         Types (0):
      (GlobalWeatherSoap12)
         Methods (2):
            GetCitiesByCountry(xs:string CountryName, )
            GetWeather(xs:string CityName, xs:string CountryName, )
         Types (0):
--------------------------------------------------------------------------------""" % (ver, build)
        self.assertEqual(string_rep, expected)

if __name__ == '__main__':
    unittest.main()
