# coding: utf-8

"""
    DFP API

    Infoblox Cloud is a SaaS offering designed to provide protection to devices on and off-premises, including roaming, remote, and branch offices. It provides visibility into infected and compromised devices, prevents DNS-based data exfiltration, and automatically stops device communications with command-and-control servers (C&Cs) and botnets, in addition to providing recursive DNS services in the cloud. You can access the services by deploying the Infoblox Endpoint agent or the DNS forwarding proxy.  For remote office deployments or in cases where installing an endpoint agent is not desirable or possible, you can use the DNS forwarding proxy. It is a software that runs on bare-metal, VM infrastructures, or Infoblox NIOS appliances; and it embeds the client IPs in DNS queries before forwarding them to Infoblox Cloud. The communications are encrypted and client visibility is maintained. The proxy also provides DNS resolution to local DNS zones when you configure local resolvers. Once you set up a DNS forwarding proxy, it becomes the main DNS server for your remote site. It will also cache responses to speed resolution of future queries.  By implementing the DNS forwarding proxy, you can rest assured that Infoblox Cloud effectively enforces DNS client-based security policies at your remote sites. On-premises devices that send DNS queries reveal their actual client IP addresses (instead of their NAT IP address), which allows Infoblox Cloud to apply the security policies applicable to the respective endpoints and identify infected clients. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dfp.api.infra_services_api import InfraServicesApi

from universal_ddi_client.api_client import ApiClient


class TestInfraServicesApi(unittest.TestCase):
    """InfraServicesApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = InfraServicesApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_create_or_update_dfp_service(self) -> None:
        """Test case for create_or_update_dfp_service

        Update DNS Forwarding Proxy services.
        """
        pass

    def test_list_dfp_services(self) -> None:
        """Test case for list_dfp_services

        List DNS Forwarding Proxy services.
        """
        pass

    def test_read_dfp_service(self) -> None:
        """Test case for read_dfp_service

        Read DNS Forwarding Proxy services.
        """
        pass


if __name__ == '__main__':
    unittest.main()
