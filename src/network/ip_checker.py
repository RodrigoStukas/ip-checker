import socket
import psutil

def obter_hostname():
    return socket.gethostname()

def obter_ip_redecorp():
    for interface, addrs in psutil.net_if_addrs().items():
        # Verifica se a interface tem info de DNS
        info = psutil.net_if_stats().get(interface)
        # psutil não traz diretamente o sufixo DNS, mas podemos filtrar pelo nome da interface
        # ou pelo IP. Como você quer pelo sufixo DNS, vamos usar ipconfig via socket.getfqdn
        fqdn = socket.getfqdn()
        if "redecorp" in fqdn.lower():
            for addr in addrs:
                if addr.family == socket.AF_INET:  # IPv4
                    return addr.address
    return None

def verificar_ip():
    ip = obter_ip_redecorp()
    hostname = obter_hostname()
    if ip:
        return f"Computador: {hostname}\nIP Corporativo: {ip}"
    else:
        return f"Computador: {hostname}\n⚠️ Ligue a VPN para obter IP corporativo"