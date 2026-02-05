import socket
import psutil

def obter_ips():
    ips = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4
                ips.append(addr.address)
    return ips

def obter_hostname():
    return socket.gethostname()

def obter_ip_redecorp():
    ips = obter_ips()
    redecorp_ips = [ip for ip in ips if ip.startswith("192.168.10.")]
    return redecorp_ips[0] if redecorp_ips else None

def verificar_ip():
    ip = obter_ip_redecorp()
    if ip:
        return f"IP: {ip}"
    else:
        return "⚠️ Ligue a VPN para obter IP corporativo"
