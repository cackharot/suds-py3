import unittest

import suds

class TestEncodeSpecials(unittest.TestCase):
    def test_specials_chars(self):
        encoder = suds.sax.Encoder()
        assert encoder.needsEncoding('&lt;test') == True # output is True
        assert encoder.encode('&lt;test') == '&amp;lt;test'
