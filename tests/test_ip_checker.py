import unittest
from src.network.ip_checker import obter_ip_redecorp, eh_rede_redecorp, obter_hostname

class TestIPChecker(unittest.TestCase):
    def test_obter_hostname(self):
        """Testa se consegue obter o hostname"""
        hostname = obter_hostname()
        self.assertIsInstance(hostname, str)
        self.assertGreater(len(hostname), 0)
    
    def test_eh_rede_redecorp(self):
        """Testa verificação de rede REDECORP"""
        resultado = eh_rede_redecorp()
        self.assertIsInstance(resultado, bool)
    
    def test_obter_ip_redecorp(self):
        """Testa obtenção de IP corporativo"""
        ip = obter_ip_redecorp()
        # Quando conectado à REDECORP, deve retornar um IP válido
        # Quando não conectado, deve retornar None
        if ip:
            # Se retornar IP, deve ser válido (começa com 10.128. ou 172.21.)
            self.assertTrue(ip.startswith("10.128.") or ip.startswith("172.21."))

if __name__ == "__main__":
    unittest.main()
