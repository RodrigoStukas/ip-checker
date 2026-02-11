import socket
import psutil
 
def obter_hostname():
    return socket.gethostname()
 
def obter_ip_redecorp():
    ips_validos = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:  
                ip = addr.address
                
                if ip.startswith("10.") or ip.startswith("172.21."):
                    ips_validos.append(ip)
    
    return ips_validos[0] if ips_validos else None
 
def verificar_ip():
    ip = obter_ip_redecorp()
    hostname = obter_hostname()
    if ip:
        return f"Computador: {hostname}\nIP Corporativo: {ip}"
    else:
        return f"Computador: {hostname}\n⚠️ Ligue a VPN para obter IP corporativo"