# encoding:utf-8
from ctpwrapper.Md import MdApiPy
import pytest
import unittest
import server_check

tcp = "tcp://180.168.146.187:10011"

@pytest.mark.skipif(server_check.check_address_port(tcp),
                    reason="180.168.146.187:10011 server can't establish")

class MdTest(unittest.TestCase):
    def test_get_version(self):
        print(MdApiPy.GetApiVersion())

    def setUp(self):
        self.investor_id = "089303"
        self.broker_id = "9999"
        self.password = "198759"
        self.md = MdApiPy()
        self.md.RegisterNameServer(tcp)

    def test_login(self):

        self.md.ReqUserLogin()
    def test_req_market_data(self):
        pass