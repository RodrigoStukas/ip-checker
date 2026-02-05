import unittest
from src.network.ip_checker import obter_ips

class TestIPChecker(unittest.TestCase):
    def test_obter_ips(self):
        ips = obter_ips()
        self.assertIsInstance(ips, list)

if __name__ == "__main__":
    unittest.main()
